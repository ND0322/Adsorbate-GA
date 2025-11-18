"""
Module potential_module


Defined at Potential.fpp lines 201-3758

This module encapsulates all the interatomic potentials implemented in QUIP

A Potential object represents an interatomic potential, a
tight binding model or an interface to an external code used to
perform calculations. It is initialised from an `args_str`
describing the type of potential, and an XML formatted string
`param_str` giving the parameters.

Types of Potential:

====================  ==========================================================
`args_str` prefix      Description
====================  ==========================================================
``IP``                Interatomic Potential
``TB``                Tight Binding Model
``FilePot``           File potential, used to communicate with external program
``CallbackPot``       Callback potential, computation done by Python function
``Sum``               Sum of two other potentials
``ForceMixing``       Combination of forces from two other potentials
====================  ==========================================================


Types of interatomic potential available:

======================== ==========================================================
`args_str` prefix        Description
======================== ==========================================================
``IP BOP``               Bond order potential for metals
``IP BornMayer``         Born-Mayer potential for oxides
(e.g. BKS potential for silica)
``IP Brenner``           Brenner(1990) potential for carbon
``IP Brenner_2002``      Brenner(2002) reactive potential for carbon
``IP Brenner_Screened``  Interface to Pastewka et al. screened Brenner reactive
potential for carbon
``IP Coulomb``           Coulomb interaction: support direct summation,
Ewald and damped shifted force Coulomb potential
``IP Einstein``          Einstein crystal potential
``IP EAM_ErcolAd``       Embedded atom potential of Ercolessi and Adams
``IP FB``                Flikkema and Bromley potential
``IP FS``                Finnis-Sinclair potential for metals
``IP FX``                Wrapper around ttm3f water potential of
Fanourgakis-Xantheas
``IP GAP``               Gaussian approximation potential
``IP Glue``              Generic implementation of 'glue' potential
``IP HFdimer``           Simple interatomic potential for an HF dimer, from
MP2 calculations
``IP KIM``               Interface to KIM, the Knowledgebase of Interatomic
potential Models(www.openkim.org)
``IP LJ``                Lennard-Jones potential
``IP Morse``             Morse potential
``IP PartridgeSchwenke`` Partridge-Schwenke model for a water monomer
``IP SW``                Stillinger-Weber potential for silicon
``IP SW_VP``             Combined Stillinger-Weber and Vashista potential
for Si and :mol:`SiO_2`.
``IP Si_MEAM``           Silicon modified embedded attom potential
``IP Sutton_Chen``       Sutton-Chen potential
``IP TS``                Tangney-Scandolo polarisable potential for oxides
``IP Tersoff``           Tersoff potential for silicon
``IP WaterDimer_Gillan`` 2-body potential for water dimer
======================== ==========================================================

Types of tight binding potential available:

======================= ==========================================================
`args_str` prefix       Description
======================= ==========================================================
``TB Bowler``           Bowler tight binding model
``TB DFTB``             Density functional tight binding
``TB GSP``              Goodwin-Skinner-Pettifor tight binding model
``TB NRL_TB``           Naval Research Laboratory tight binding model
======================= ==========================================================

Examples of the XML parameters for each of these potential can be
found in the `src/Parameters <https://github.com/libAtoms/QUIP/tree/public/share/Parameters>`_
directory of the QUIP git repository.


"""
from __future__ import print_function, absolute_import, division
import quippy._quippy
import f90wrap.runtime
import logging
import numpy
from quippy.dictionary_module import Dictionary
from quippy.system_module import InOutput
from quippy.atoms_types_module import Atoms
from quippy.potential_simple_module import Potential_Simple

_arrays = {}
_objs = {}

@f90wrap.runtime.register_class("quippy.Potential")
class Potential(f90wrap.runtime.FortranDerivedType):
    """
    Type(name=potential)
    
    
    Defined at Potential.fpp lines 283-299
    
    """
    @classmethod
    def filename_initialise(cls, args_str, param_filename, bulk_scale=None, error=None):
        """
        self = Potential(args_str, param_filename[, bulk_scale, error])
        
        
        Defined at Potential.fpp lines 676-697
        
        Parameters
        ----------
        args_str : str
        	Valid arguments are 'Sum', 'ForceMixing', 'EVB', 'Local_E_Mix' and 'ONIOM', and any type of simple_potential
        
        param_filename : str
        	name of xml parameter file for potential initializers
        
        bulk_scale : Atoms
        	optional bulk structure for calculating space and E rescaling
        
        error : int
        
        Returns
        -------
        this : Potential
        
        """
        bare_class = cls.__new__(cls)
        f90wrap.runtime.FortranDerivedType.__init__(bare_class)
        result = quippy._quippy.f90wrap_potential_filename_initialise(args_str=args_str, param_filename=param_filename, \
            bulk_scale=None if bulk_scale is None else bulk_scale._handle, error=error)
        bare_class._handle = result[0] if isinstance(result, tuple) else result
        return bare_class
    
    def __init__(self, args_str=None, pot1=None, pot2=None, param_str=None, bulk_scale=None, error=None, handle=None):
        """
        self = Potential([args_str, pot1, pot2, param_str, bulk_scale, error])
        
        
        Defined at Potential.fpp lines 722-902
        
        Parameters
        ----------
        args_str : str
        	Valid arguments are 'Sum', 'ForceMixing', 'EVB', 'Local_E_Mix' and 'ONIOM', and any type of simple_potential
        
        pot1 : Potential
        	Optional first Potential upon which this Potential is based
        
        pot2 : Potential
        	Optional second potential
        
        param_str : str
        	contents of xml parameter file for potential initializers, if needed
        
        bulk_scale : Atoms
        	optional bulk structure for calculating space and E rescaling
        
        error : int
        
        Returns
        -------
        this : Potential
        
        Potential type which abstracts all QUIP interatomic potentials
        
        Provides interface to all energy/force/virial calculating schemes,
        including actual calculations, as well as abstract hybrid schemes
        such as LOTF, Force Mixing, ONIOM, and the local energy scheme.
        
        Typically a Potential is constructed from an initialisation
        args_str and an XML parameter file, e.g. in Fortran::
        
        type(InOutput) :: xml_file
        type(Potential) :: pot
        ...
        call initialise(xml_file, 'SW.xml', INPUT)
        call initialise(pot, 'IP SW', param_file=xml_file)
        
        Or, equivaently in Python::
        
        pot = Potential('IP SW', param_filename='SW.xml')
        
        creates a Stillinger-Weber potential using the parameters from
        the file 'SW.xml'. The XML parameters can also be given directly
        as a string, via the `param_str` argument.
        
        The main workhorse is the :meth:`calc` routine, which is used
        internally to perform all calculations, e.g. to calculate forces::
        
        type(Atoms) :: at
        real(dp) :: force(3,8)
        ...
        call diamond(at, 5.44, 14)
        call randomise(at%pos, 0.01)
        call calc(pot, at, force=force)
        
        Note that there is now no need to set the 'Atoms%cutoff' attribute to the
        cutoff of this Potential: if it is less than this it will be increased
        automatically and a warning will be printed.
        The neighbour lists are updated automatically with the
        :meth:`~quippy.atoms.Atoms.calc_connect` routine. For efficiency,
        it's a good idea to set at%cutoff_skin greater than zero to decrease
        the frequency at which the connectivity needs to be rebuilt.
        
        A Potential can be used to optimise the geometry of an
        :class:`~quippy.atoms.Atoms` structure, using the :meth:`minim` routine,
        (or, in Python, via  the :class:`Minim` wrapper class).
        
        .. rubric:: args_str options
        
        ============== ===== ===== ============================================================================
        Name           Type  Value Doc                                                                         
        ============== ===== ===== ============================================================================
        xml_label      None        Label in xml file Potential stanza to match                                 
        calc_args      None        Default calc_args that are passed each time calc() is called                
        init_args_pot1 None        Argument string for initializing pot1(for non-simple potentials             
        init_args_pot2 None        Argument string for initializing pot2(for non-simple potentials             
        Sum            None  false Potential that's a sum of 2 other potentials                                
        ForceMixing    None  false Potential that's force-mixing of 2 other potentials                         
        EVB            None  false Potential using empirical-valence bond to mix 2 other potentials            
        Cluster        None  false Potential evaluated using clusters                                          
        do_rescale_r   bool  F     If true, rescale distances by factor r_scale.                               
        r_scale        float 1.0   Recaling factor for distances. Default 1.0.                                 
        do_rescale_E   bool  F     If true, rescale energy by factor E_scale.                                  
        E_scale        float 1.0   Recaling factor for energy. Default 1.0.                                    
        minimise_bulk  bool  F     If true, minimise bulk_scale structure before measuring eqm. volume and     
                                   bulk modulus for rescaling                                                  
        target_vol     float 0.0   Target volume per cell used if do_rescale_r=T Unit is A^3.                  
        target_B       float 0.0   Target bulk modulus used if do_rescale_E=T. Unit is GPa.                    
        ============== ===== ===== ============================================================================
        
        
        """
        f90wrap.runtime.FortranDerivedType.__init__(self)
        result = quippy._quippy.f90wrap_potential_initialise(args_str=args_str, pot1=(None if pot1 is None else pot1._handle), \
            pot2=(None if pot2 is None else pot2._handle), param_str=param_str, bulk_scale=(None if bulk_scale is None else \
            bulk_scale._handle), error=error)
        self._handle = result[0] if isinstance(result, tuple) else result
    
    def __del__(self, error=None):
        """
        Destructor for class Potential
        
        
        Defined at Potential.fpp lines 904-932
        
        Parameters
        ----------
        this : Potential
        error : int
        
        """
        if self._alloc:
            quippy._quippy.f90wrap_potential_finalise(this=self._handle, error=error)
    
    def setup_parallel(self, at, args_str, error=None):
        """
        setup_parallel(self, at, args_str[, error])
        
        
        Defined at Potential.fpp lines 1103-1111
        
        Parameters
        ----------
        this : Potential
        at : Atoms
        	The atoms structure to compute energy and forces
        
        args_str : str
        error : int
        
        """
        quippy._quippy.f90wrap_potential_setup_parallel(this=self._handle, at=at._handle, args_str=args_str, error=error)
    
    def print(self, file=None, dict=None, error=None):
        """
        print(self[, file, dict, error])
        
        
        Defined at Potential.fpp lines 1113-1133
        
        Parameters
        ----------
        this : Potential
        file : Inoutput
        dict : Dictionary
        error : int
        
        """
        quippy._quippy.f90wrap_potential_print(this=self._handle, file=None if file is None else file._handle, dict=None if dict \
            is None else dict._handle, error=error)
    
    def cutoff(self, error=None):
        """
        potential_cutoff = cutoff(self[, error])
        
        
        Defined at Potential.fpp lines 1135-1153
        
        Parameters
        ----------
        this : Potential
        error : int
        
        Returns
        -------
        potential_cutoff : float
        
        Return the cutoff of this 'Potential', in Angstrom. This is the
        minimum neighbour connectivity cutoff that should be used: if
        you're doing MD you'll want to use a slightly larger cutoff so
        that new neighbours don't drift in to range between connectivity
        updates
        """
        potential_cutoff = quippy._quippy.f90wrap_potential_cutoff(this=self._handle, error=error)
        return potential_cutoff
    
    def calc(self, at, energy=None, force=None, virial=None, local_energy=None, local_virial=None, args_str=None, \
        error=None):
        """
        calc(self, at[, energy, force, virial, local_energy, local_virial, args_str, error])
        
        
        Defined at Potential.fpp lines 934-1101
        
        Parameters
        ----------
        this : Potential
        at : Atoms
        energy : float
        force : float array
        virial : float array
        local_energy : float array
        local_virial : float array
        args_str : str
        error : int
        
        Apply this Potential to the Atoms object
        'at'. Atoms%calc_connect is automatically called to update the
        connecticvity information -- if efficiency is important to you,
        ensure that at%cutoff_skin is set to a non-zero value to decrease
        the frequence of connectivity updates.
        optional arguments determine what should be calculated and how
        it will be returned. Each physical quantity has a
        corresponding optional argument, which can either be an 'True'
        to store the result inside the Atoms object(i.e. in
        Atoms%params' or in 'Atoms%properties' with the
        default name, a string to specify a different property or
        parameter name, or an array of the the correct shape to
        receive the quantity in question, as set out in the table
        below.
        
        ================  ============= ================ =========================
        Array argument    Quantity      Shape            Default storage location
        ================  ============= ================ =========================
        ``energy``        Energy        ``()``                  ``energy`` param
        ``local_energy``  Local energy  ``(at.n,)``      ``local_energy`` property
        ``force``         Force         ``(3,at.n)``     ``force`` property
        ``virial``        Virial tensor ``(3,3)``        ``virial`` param
        ``local_virial``  Local virial  ``(3,3,at.n)``   ``local_virial`` property
        ================  ============= ================ =========================
        
        The 'args_str' argument is an optional string  containing
        additional arguments which depend on the particular Potential
        being used.
        
        Not all Potentials support all of these quantities: an error
        will be raised if you ask for something that is not supported.
        
        .. rubric:: args_str options
        
        =============== ===== ===== ===========================================================================
        Name            Type  Value Doc                                                                        
        =============== ===== ===== ===========================================================================
        energy          None        If present, calculate energy and put it in field with this string as name  
        virial          None        If present, calculate virial and put it in field with this string as name  
        force           None        If present, calculate force and put it in field with this string as name   
        local_energy    None        If present, calculate local energy and put it in field with this string as 
                                    name                                                                       
        local_virial    None        If present, calculate local virial and put it in field with this string as 
                                    name                                                                       
        r_scale         float 0.0   Distance rescale factor. Overrides r_scale init arg                        
        E_scale         float 0.0   Energy rescale factor. Overrides E_scale init arg                          
        do_calc_connect bool  T     Switch on/off automatic calc_connect() calls.                              
        =============== ===== ===== ===========================================================================
        
        
        """
        quippy._quippy.f90wrap_potential_calc(this=self._handle, at=at._handle, energy=energy, force=force, virial=virial, \
            local_energy=local_energy, local_virial=local_virial, args_str=args_str, error=error)
    
    def minim(self, at, method, convergence_tol, max_steps, linminroutine=None, do_print=None, print_inoutput=None, \
        do_pos=None, do_lat=None, args_str=None, eps_guess=None, fire_minim_dt0=None, fire_minim_dt_max=None, \
        external_pressure=None, use_precond=None, hook_print_interval=None, error=None):
        """
        potential_minim = minim(self, at, method, convergence_tol, max_steps[, linminroutine, do_print, print_inoutput, do_pos, \
            do_lat, args_str, eps_guess, fire_minim_dt0, fire_minim_dt_max, external_pressure, use_precond, hook_print_interval, \
            error])
        
        
        Defined at Potential.fpp lines 1182-1325
        
        Parameters
        ----------
        this : Potential
        	potential to evaluate energy/forces with
        
        at : Atoms
        	starting configuration
        
        method : str
        	passed to minim()
        
        convergence_tol : float
        	Minimisation is treated as converged once $|\mathbf{\nabla}f|^2 <$
        	'convergence_tol'.
        
        max_steps : int
        	Maximum number of steps
        
        linminroutine : str
        	Name of the line minisation routine to use, passed to base minim()
        
        do_print : bool
        	if true, print configurations using minim's hook()
        
        print_inoutput : Inoutput
        	inoutput object to print configs to, needed if do_print is true
        
        do_pos : bool
        	do relaxation w.r.t. positions and/or lattice(if neither is included, do both)
        
        do_lat : bool
        	do relaxation w.r.t. positions and/or lattice(if neither is included, do both)
        
        args_str : str
        	arguments to pass to calc()
        
        eps_guess : float
        	eps_guess argument to pass to minim
        
        fire_minim_dt0 : float
        	if using fire minim, initial value for time step
        
        fire_minim_dt_max : float
        	if using fire minim, max value for time step
        
        external_pressure : float array
        use_precond : bool
        hook_print_interval : int
        	how often to print xyz from hook function
        
        error : int
        	set to 1 if an error occurred during minimisation
        
        
        Returns
        -------
        potential_minim : int
        
        Minimise the configuration 'at' under the action of this
        Potential.  Returns number of minimisation steps taken. If
        an error occurs or convergence is not reached within 'max_steps'
        steps, 'status' will be set to 1 on exit.
        
        Example usage(in Python, Fortran code is similar. See
        :ref:`geomopt` in the quippy tutorial for full
        explanation)::
        
        >      at0 = diamond(5.44, 14)
        >      pot = Potential('IP SW', param_str='''<SW_params n_types="1">
        >              <comment> Stillinger and Weber, Phys. Rev. B  31 p 5262(1984)</comment>
        >              <per_type_data type="1" atomic_num="14" />
        >
        >              <per_pair_data atnum_i="14" atnum_j="14" AA="7.049556277" BB="0.6022245584"
        >                p="4" q="0" a="1.80" sigma="2.0951" eps="2.1675" />
        >
        >              <per_triplet_data atnum_c="14" atnum_j="14" atnum_k="14"
        >                lambda="21.0" gamma="1.20" eps="2.1675" />
        >             </SW_params>''')
        >      pot.minim(at0, 'cg', 1e-7, 100, do_pos=True, do_lat=True)
        """
        potential_minim = quippy._quippy.f90wrap_potential_minim(this=self._handle, at=at._handle, method=method, \
            convergence_tol=convergence_tol, max_steps=max_steps, linminroutine=linminroutine, do_print=do_print, \
            print_inoutput=None if print_inoutput is None else print_inoutput._handle, do_pos=do_pos, do_lat=do_lat, \
            args_str=args_str, eps_guess=eps_guess, fire_minim_dt0=fire_minim_dt0, fire_minim_dt_max=fire_minim_dt_max, \
            external_pressure=external_pressure, use_precond=use_precond, hook_print_interval=hook_print_interval, error=error)
        return potential_minim
    
    def pot_test_gradient(self, at, do_pos=None, do_lat=None, args_str=None, dir_field=None):
        """
        pot_test_gradient = pot_test_gradient(self, at[, do_pos, do_lat, args_str, dir_field])
        
        
        Defined at Potential.fpp lines 1388-1447
        
        Parameters
        ----------
        pot : Potential
        at : Atoms
        do_pos : bool
        do_lat : bool
        args_str : str
        dir_field : str
        
        Returns
        -------
        pot_test_gradient : bool
        
        """
        pot_test_gradient = quippy._quippy.f90wrap_pot_test_gradient(pot=self._handle, at=at._handle, do_pos=do_pos, \
            do_lat=do_lat, args_str=args_str, dir_field=dir_field)
        return pot_test_gradient
    
    def pot_n_test_gradient(self, at, do_pos=None, do_lat=None, args_str=None, dir_field=None):
        """
        pot_n_test_gradient(self, at[, do_pos, do_lat, args_str, dir_field])
        
        
        Defined at Potential.fpp lines 1450-1507
        
        Parameters
        ----------
        pot : Potential
        at : Atoms
        do_pos : bool
        do_lat : bool
        args_str : str
        dir_field : str
        
        """
        quippy._quippy.f90wrap_pot_n_test_gradient(pot=self._handle, at=at._handle, do_pos=do_pos, do_lat=do_lat, \
            args_str=args_str, dir_field=dir_field)
    
    def bulk_modulus(self, at, minimise_bulk=None, eps=None, args_str=None):
        """
        b, v0 = bulk_modulus(self, at[, minimise_bulk, eps, args_str])
        
        
        Defined at Potential.fpp lines 3439-3479
        
        Parameters
        ----------
        pot : Potential
        at : Atoms
        minimise_bulk : bool
        eps : float
        args_str : str
        
        Returns
        -------
        b : float
        v0 : float
        
        """
        b, v0 = quippy._quippy.f90wrap_potential_bulk_modulus(pot=self._handle, at=at._handle, minimise_bulk=minimise_bulk, \
            eps=eps, args_str=args_str)
        return b, v0
    
    def test_local_virial(self, at, args_str=None):
        """
        test_local_virial(self, at[, args_str])
        
        
        Defined at Potential.fpp lines 1327-1378
        
        Parameters
        ----------
        this : Potential
        at : Atoms
        args_str : str
        
        """
        quippy._quippy.f90wrap_potential_test_local_virial(this=self._handle, at=at._handle, args_str=args_str)
    
    def calc_tb_matrices(self, at, args_str=None, hd=None, sd=None, hz=None, sz=None, dh=None, ds=None, index_bn=None):
        """
        calc_tb_matrices(self, at[, args_str, hd, sd, hz, sz, dh, ds, index_bn])
        
        
        Defined at Potential.fpp lines 2098-2110
        
        Parameters
        ----------
        this : Potential
        at : Atoms
        	Atomic structure to use for TB matrix calculation
        
        args_str : str
        	Additional arguments to pass to TB `calc()` routine
        
        hd : float array
        	Hamiltonian and overlap for real wavefunctions(gamma point)
        
        sd : float array
        	Hamiltonian and overlap for real wavefunctions(gamma point)
        
        hz : complex array
        	Complex Hamiltonian and overlap(multiple kpoints)
        
        sz : complex array
        	Complex Hamiltonian and overlap(multiple kpoints)
        
        dh : float array
        	Derivative of H and S wrt atomic positiions. Shape is `(3, N_atoms, N_elecs, N_elecs)`
        
        ds : float array
        	Derivative of H and S wrt atomic positiions. Shape is `(3, N_atoms, N_elecs, N_elecs)`
        
        index_bn : int
        
        Calculate TB Hamiltonian and overlap matrices and optionally their derivatives wrt atomic positions.
        This always triggers a force calculation, since the elements for dH and dS are assembled on the fly for each atom.
        """
        quippy._quippy.f90wrap_potential_calc_tb_matrices(this=self._handle, at=at._handle, args_str=args_str, hd=hd, sd=sd, \
            hz=hz, sz=sz, dh=dh, ds=ds, index_bn=index_bn)
    
    @property
    def init_args_pot1(self):
        """
        Element init_args_pot1 ftype=character(len=string_length) pytype=str
        
        
        Defined at Potential.fpp line 285
        
        """
        return quippy._quippy.f90wrap_potential__get__init_args_pot1(self._handle)
    
    @init_args_pot1.setter
    def init_args_pot1(self, init_args_pot1):
        quippy._quippy.f90wrap_potential__set__init_args_pot1(self._handle, init_args_pot1)
    
    @property
    def init_args_pot2(self):
        """
        Element init_args_pot2 ftype=character(len=string_length) pytype=str
        
        
        Defined at Potential.fpp line 285
        
        """
        return quippy._quippy.f90wrap_potential__get__init_args_pot2(self._handle)
    
    @init_args_pot2.setter
    def init_args_pot2(self, init_args_pot2):
        quippy._quippy.f90wrap_potential__set__init_args_pot2(self._handle, init_args_pot2)
    
    @property
    def xml_label(self):
        """
        Element xml_label ftype=character(len=string_length) pytype=str
        
        
        Defined at Potential.fpp line 285
        
        """
        return quippy._quippy.f90wrap_potential__get__xml_label(self._handle)
    
    @xml_label.setter
    def xml_label(self, xml_label):
        quippy._quippy.f90wrap_potential__set__xml_label(self._handle, xml_label)
    
    @property
    def xml_init_args(self):
        """
        Element xml_init_args ftype=character(len=string_length) pytype=str
        
        
        Defined at Potential.fpp line 285
        
        """
        return quippy._quippy.f90wrap_potential__get__xml_init_args(self._handle)
    
    @xml_init_args.setter
    def xml_init_args(self, xml_init_args):
        quippy._quippy.f90wrap_potential__set__xml_init_args(self._handle, xml_init_args)
    
    @property
    def calc_args(self):
        """
        Element calc_args ftype=character(len=string_length) pytype=str
        
        
        Defined at Potential.fpp line 285
        
        """
        return quippy._quippy.f90wrap_potential__get__calc_args(self._handle)
    
    @calc_args.setter
    def calc_args(self, calc_args):
        quippy._quippy.f90wrap_potential__set__calc_args(self._handle, calc_args)
    
    @property
    def is_simple(self):
        """
        Element is_simple ftype=logical pytype=bool
        
        
        Defined at Potential.fpp line 286
        
        """
        return quippy._quippy.f90wrap_potential__get__is_simple(self._handle)
    
    @is_simple.setter
    def is_simple(self, is_simple):
        quippy._quippy.f90wrap_potential__set__is_simple(self._handle, is_simple)
    
    @property
    def simple(self):
        """
        Element simple ftype=type(potential_simple) pytype=Potential_Simple
        
        
        Defined at Potential.fpp line 287
        
        """
        simple_handle = quippy._quippy.f90wrap_potential__get__simple(self._handle)
        if tuple(simple_handle) in self._objs:
            simple = self._objs[tuple(simple_handle)]
        else:
            simple = Potential_Simple.from_handle(simple_handle)
            self._objs[tuple(simple_handle)] = simple
        return simple
    
    @simple.setter
    def simple(self, simple):
        simple = simple._handle
        quippy._quippy.f90wrap_potential__set__simple(self._handle, simple)
    
    @property
    def l_mpot1(self):
        """
        Element l_mpot1 ftype=type(potential) pytype=Potential
        
        
        Defined at Potential.fpp line 288
        
        """
        l_mpot1_handle = quippy._quippy.f90wrap_potential__get__l_mpot1(self._handle)
        if tuple(l_mpot1_handle) in self._objs:
            l_mpot1 = self._objs[tuple(l_mpot1_handle)]
        else:
            l_mpot1 = Potential.from_handle(l_mpot1_handle)
            self._objs[tuple(l_mpot1_handle)] = l_mpot1
        return l_mpot1
    
    @l_mpot1.setter
    def l_mpot1(self, l_mpot1):
        l_mpot1 = l_mpot1._handle
        quippy._quippy.f90wrap_potential__set__l_mpot1(self._handle, l_mpot1)
    
    @property
    def l_mpot2(self):
        """
        Element l_mpot2 ftype=type(potential) pytype=Potential
        
        
        Defined at Potential.fpp line 289
        
        """
        l_mpot2_handle = quippy._quippy.f90wrap_potential__get__l_mpot2(self._handle)
        if tuple(l_mpot2_handle) in self._objs:
            l_mpot2 = self._objs[tuple(l_mpot2_handle)]
        else:
            l_mpot2 = Potential.from_handle(l_mpot2_handle)
            self._objs[tuple(l_mpot2_handle)] = l_mpot2
        return l_mpot2
    
    @l_mpot2.setter
    def l_mpot2(self, l_mpot2):
        l_mpot2 = l_mpot2._handle
        quippy._quippy.f90wrap_potential__set__l_mpot2(self._handle, l_mpot2)
    
    @property
    def is_sum(self):
        """
        Element is_sum ftype=logical pytype=bool
        
        
        Defined at Potential.fpp line 290
        
        """
        return quippy._quippy.f90wrap_potential__get__is_sum(self._handle)
    
    @is_sum.setter
    def is_sum(self, is_sum):
        quippy._quippy.f90wrap_potential__set__is_sum(self._handle, is_sum)
    
    @property
    def sum(self):
        """
        Element sum ftype=type(potential_sum) pytype=Potential_Sum
        
        
        Defined at Potential.fpp line 291
        
        """
        sum_handle = quippy._quippy.f90wrap_potential__get__sum(self._handle)
        if tuple(sum_handle) in self._objs:
            sum = self._objs[tuple(sum_handle)]
        else:
            sum = Potential_Sum.from_handle(sum_handle)
            self._objs[tuple(sum_handle)] = sum
        return sum
    
    @sum.setter
    def sum(self, sum):
        sum = sum._handle
        quippy._quippy.f90wrap_potential__set__sum(self._handle, sum)
    
    @property
    def is_forcemixing(self):
        """
        Element is_forcemixing ftype=logical pytype=bool
        
        
        Defined at Potential.fpp line 292
        
        """
        return quippy._quippy.f90wrap_potential__get__is_forcemixing(self._handle)
    
    @is_forcemixing.setter
    def is_forcemixing(self, is_forcemixing):
        quippy._quippy.f90wrap_potential__set__is_forcemixing(self._handle, is_forcemixing)
    
    @property
    def forcemixing(self):
        """
        Element forcemixing ftype=type(potential_fm) pytype=Potential_Fm
        
        
        Defined at Potential.fpp line 293
        
        """
        forcemixing_handle = quippy._quippy.f90wrap_potential__get__forcemixing(self._handle)
        if tuple(forcemixing_handle) in self._objs:
            forcemixing = self._objs[tuple(forcemixing_handle)]
        else:
            forcemixing = Potential_FM.from_handle(forcemixing_handle)
            self._objs[tuple(forcemixing_handle)] = forcemixing
        return forcemixing
    
    @forcemixing.setter
    def forcemixing(self, forcemixing):
        forcemixing = forcemixing._handle
        quippy._quippy.f90wrap_potential__set__forcemixing(self._handle, forcemixing)
    
    @property
    def is_evb(self):
        """
        Element is_evb ftype=logical pytype=bool
        
        
        Defined at Potential.fpp line 294
        
        """
        return quippy._quippy.f90wrap_potential__get__is_evb(self._handle)
    
    @is_evb.setter
    def is_evb(self, is_evb):
        quippy._quippy.f90wrap_potential__set__is_evb(self._handle, is_evb)
    
    @property
    def evb(self):
        """
        Element evb ftype=type(potential_evb) pytype=Potential_Evb
        
        
        Defined at Potential.fpp line 295
        
        """
        evb_handle = quippy._quippy.f90wrap_potential__get__evb(self._handle)
        if tuple(evb_handle) in self._objs:
            evb = self._objs[tuple(evb_handle)]
        else:
            evb = Potential_EVB.from_handle(evb_handle)
            self._objs[tuple(evb_handle)] = evb
        return evb
    
    @evb.setter
    def evb(self, evb):
        evb = evb._handle
        quippy._quippy.f90wrap_potential__set__evb(self._handle, evb)
    
    @property
    def is_cluster(self):
        """
        Element is_cluster ftype=logical pytype=bool
        
        
        Defined at Potential.fpp line 296
        
        """
        return quippy._quippy.f90wrap_potential__get__is_cluster(self._handle)
    
    @is_cluster.setter
    def is_cluster(self, is_cluster):
        quippy._quippy.f90wrap_potential__set__is_cluster(self._handle, is_cluster)
    
    @property
    def cluster(self):
        """
        Element cluster ftype=type(potential_cluster) pytype=Potential_Cluster
        
        
        Defined at Potential.fpp line 297
        
        """
        cluster_handle = quippy._quippy.f90wrap_potential__get__cluster(self._handle)
        if tuple(cluster_handle) in self._objs:
            cluster = self._objs[tuple(cluster_handle)]
        else:
            cluster = Potential_Cluster.from_handle(cluster_handle)
            self._objs[tuple(cluster_handle)] = cluster
        return cluster
    
    @cluster.setter
    def cluster(self, cluster):
        cluster = cluster._handle
        quippy._quippy.f90wrap_potential__set__cluster(self._handle, cluster)
    
    @property
    def do_rescale_r(self):
        """
        Element do_rescale_r ftype=logical pytype=bool
        
        
        Defined at Potential.fpp line 298
        
        """
        return quippy._quippy.f90wrap_potential__get__do_rescale_r(self._handle)
    
    @do_rescale_r.setter
    def do_rescale_r(self, do_rescale_r):
        quippy._quippy.f90wrap_potential__set__do_rescale_r(self._handle, do_rescale_r)
    
    @property
    def do_rescale_e(self):
        """
        Element do_rescale_e ftype=logical pytype=bool
        
        
        Defined at Potential.fpp line 298
        
        """
        return quippy._quippy.f90wrap_potential__get__do_rescale_e(self._handle)
    
    @do_rescale_e.setter
    def do_rescale_e(self, do_rescale_e):
        quippy._quippy.f90wrap_potential__set__do_rescale_e(self._handle, do_rescale_e)
    
    @property
    def r_scale(self):
        """
        Element r_scale ftype=real(dp) pytype=float
        
        
        Defined at Potential.fpp line 299
        
        """
        return quippy._quippy.f90wrap_potential__get__r_scale(self._handle)
    
    @r_scale.setter
    def r_scale(self, r_scale):
        quippy._quippy.f90wrap_potential__set__r_scale(self._handle, r_scale)
    
    @property
    def e_scale(self):
        """
        Element e_scale ftype=real(dp) pytype=float
        
        
        Defined at Potential.fpp line 299
        
        """
        return quippy._quippy.f90wrap_potential__get__e_scale(self._handle)
    
    @e_scale.setter
    def e_scale(self, e_scale):
        quippy._quippy.f90wrap_potential__set__e_scale(self._handle, e_scale)
    
    def __str__(self):
        ret = ['<potential>{\n']
        ret.append('    init_args_pot1 : ')
        ret.append(repr(self.init_args_pot1))
        ret.append(',\n    init_args_pot2 : ')
        ret.append(repr(self.init_args_pot2))
        ret.append(',\n    xml_label : ')
        ret.append(repr(self.xml_label))
        ret.append(',\n    xml_init_args : ')
        ret.append(repr(self.xml_init_args))
        ret.append(',\n    calc_args : ')
        ret.append(repr(self.calc_args))
        ret.append(',\n    is_simple : ')
        ret.append(repr(self.is_simple))
        ret.append(',\n    simple : ')
        ret.append(repr(self.simple))
        ret.append(',\n    l_mpot1 : ')
        ret.append(repr(self.l_mpot1))
        ret.append(',\n    l_mpot2 : ')
        ret.append(repr(self.l_mpot2))
        ret.append(',\n    is_sum : ')
        ret.append(repr(self.is_sum))
        ret.append(',\n    sum : ')
        ret.append(repr(self.sum))
        ret.append(',\n    is_forcemixing : ')
        ret.append(repr(self.is_forcemixing))
        ret.append(',\n    forcemixing : ')
        ret.append(repr(self.forcemixing))
        ret.append(',\n    is_evb : ')
        ret.append(repr(self.is_evb))
        ret.append(',\n    evb : ')
        ret.append(repr(self.evb))
        ret.append(',\n    is_cluster : ')
        ret.append(repr(self.is_cluster))
        ret.append(',\n    cluster : ')
        ret.append(repr(self.cluster))
        ret.append(',\n    do_rescale_r : ')
        ret.append(repr(self.do_rescale_r))
        ret.append(',\n    do_rescale_e : ')
        ret.append(repr(self.do_rescale_e))
        ret.append(',\n    r_scale : ')
        ret.append(repr(self.r_scale))
        ret.append(',\n    e_scale : ')
        ret.append(repr(self.e_scale))
        ret.append('}')
        return ''.join(ret)
    
    _dt_array_initialisers = []
    

@f90wrap.runtime.register_class("quippy.Potential_minimise")
class Potential_minimise(f90wrap.runtime.FortranDerivedType):
    """
    Type(name=potential_minimise)
    
    
    Defined at Potential.fpp lines 409-421
    
    """
    def __init__(self, handle=None):
        """
        self = Potential_Minimise()
        
        
        Defined at Potential.fpp lines 409-421
        
        
        Returns
        -------
        this : Potential_Minimise
        	Object to be constructed
        
        
        Automatically generated constructor for potential_minimise
        """
        f90wrap.runtime.FortranDerivedType.__init__(self)
        result = quippy._quippy.f90wrap_potential_minimise_initialise()
        self._handle = result[0] if isinstance(result, tuple) else result
    
    def __del__(self):
        """
        Destructor for class Potential_Minimise
        
        
        Defined at Potential.fpp lines 409-421
        
        Parameters
        ----------
        this : Potential_Minimise
        	Object to be destructed
        
        
        Automatically generated destructor for potential_minimise
        """
        if self._alloc:
            quippy._quippy.f90wrap_potential_minimise_finalise(this=self._handle)
    
    @property
    def minim_pos_lat_preconditioner(self):
        """
        Element minim_pos_lat_preconditioner ftype=real(dp) pytype=float
        
        
        Defined at Potential.fpp line 410
        
        """
        return quippy._quippy.f90wrap_potential_minimise__get__minim_pos_lat_preconditioner(self._handle)
    
    @minim_pos_lat_preconditioner.setter
    def minim_pos_lat_preconditioner(self, minim_pos_lat_preconditioner):
        quippy._quippy.f90wrap_potential_minimise__set__minim_pos_lat_preconditioner(self._handle, minim_pos_lat_preconditioner)
    
    @property
    def minim_save_lat(self):
        """
        Element minim_save_lat ftype=real(dp) pytype=float
        
        
        Defined at Potential.fpp line 411
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            quippy._quippy.f90wrap_potential_minimise__array__minim_save_lat(self._handle)
        if array_handle in self._arrays:
            minim_save_lat = self._arrays[array_handle]
        else:
            minim_save_lat = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    self._handle,
                                    quippy._quippy.f90wrap_potential_minimise__array__minim_save_lat)
            self._arrays[array_handle] = minim_save_lat
        return minim_save_lat
    
    @minim_save_lat.setter
    def minim_save_lat(self, minim_save_lat):
        self.minim_save_lat[...] = minim_save_lat
    
    @property
    def minim_args_str(self):
        """
        Element minim_args_str ftype=character(len=string_length) pytype=str
        
        
        Defined at Potential.fpp line 412
        
        """
        return quippy._quippy.f90wrap_potential_minimise__get__minim_args_str(self._handle)
    
    @minim_args_str.setter
    def minim_args_str(self, minim_args_str):
        quippy._quippy.f90wrap_potential_minimise__set__minim_args_str(self._handle, minim_args_str)
    
    @property
    def minim_do_pos(self):
        """
        Element minim_do_pos ftype=logical pytype=bool
        
        
        Defined at Potential.fpp line 413
        
        """
        return quippy._quippy.f90wrap_potential_minimise__get__minim_do_pos(self._handle)
    
    @minim_do_pos.setter
    def minim_do_pos(self, minim_do_pos):
        quippy._quippy.f90wrap_potential_minimise__set__minim_do_pos(self._handle, minim_do_pos)
    
    @property
    def minim_do_lat(self):
        """
        Element minim_do_lat ftype=logical pytype=bool
        
        
        Defined at Potential.fpp line 413
        
        """
        return quippy._quippy.f90wrap_potential_minimise__get__minim_do_lat(self._handle)
    
    @minim_do_lat.setter
    def minim_do_lat(self, minim_do_lat):
        quippy._quippy.f90wrap_potential_minimise__set__minim_do_lat(self._handle, minim_do_lat)
    
    @property
    def minim_n_eval_e(self):
        """
        Element minim_n_eval_e ftype=integer  pytype=int
        
        
        Defined at Potential.fpp line 414
        
        """
        return quippy._quippy.f90wrap_potential_minimise__get__minim_n_eval_e(self._handle)
    
    @minim_n_eval_e.setter
    def minim_n_eval_e(self, minim_n_eval_e):
        quippy._quippy.f90wrap_potential_minimise__set__minim_n_eval_e(self._handle, minim_n_eval_e)
    
    @property
    def minim_n_eval_f(self):
        """
        Element minim_n_eval_f ftype=integer  pytype=int
        
        
        Defined at Potential.fpp line 414
        
        """
        return quippy._quippy.f90wrap_potential_minimise__get__minim_n_eval_f(self._handle)
    
    @minim_n_eval_f.setter
    def minim_n_eval_f(self, minim_n_eval_f):
        quippy._quippy.f90wrap_potential_minimise__set__minim_n_eval_f(self._handle, minim_n_eval_f)
    
    @property
    def minim_n_eval_ef(self):
        """
        Element minim_n_eval_ef ftype=integer  pytype=int
        
        
        Defined at Potential.fpp line 414
        
        """
        return quippy._quippy.f90wrap_potential_minimise__get__minim_n_eval_ef(self._handle)
    
    @minim_n_eval_ef.setter
    def minim_n_eval_ef(self, minim_n_eval_ef):
        quippy._quippy.f90wrap_potential_minimise__set__minim_n_eval_ef(self._handle, minim_n_eval_ef)
    
    @property
    def pos_lat_preconditioner_factor(self):
        """
        Element pos_lat_preconditioner_factor ftype=real(dp) pytype=float
        
        
        Defined at Potential.fpp line 415
        
        """
        return quippy._quippy.f90wrap_potential_minimise__get__pos_lat_preconditioner_factor(self._handle)
    
    @pos_lat_preconditioner_factor.setter
    def pos_lat_preconditioner_factor(self, pos_lat_preconditioner_factor):
        quippy._quippy.f90wrap_potential_minimise__set__pos_lat_preconditioner_factor(self._handle, \
            pos_lat_preconditioner_factor)
    
    @property
    def minim_at(self):
        """
        Element minim_at ftype=type(atoms) pytype=Atoms
        
        
        Defined at Potential.fpp line 416
        
        """
        minim_at_handle = quippy._quippy.f90wrap_potential_minimise__get__minim_at(self._handle)
        if tuple(minim_at_handle) in self._objs:
            minim_at = self._objs[tuple(minim_at_handle)]
        else:
            minim_at = Atoms.from_handle(minim_at_handle)
            self._objs[tuple(minim_at_handle)] = minim_at
        return minim_at
    
    @minim_at.setter
    def minim_at(self, minim_at):
        minim_at = minim_at._handle
        quippy._quippy.f90wrap_potential_minimise__set__minim_at(self._handle, minim_at)
    
    @property
    def last_connect_x(self):
        """
        Element last_connect_x ftype=real(dp) pytype=float
        
        
        Defined at Potential.fpp line 417
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            quippy._quippy.f90wrap_potential_minimise__array__last_connect_x(self._handle)
        if array_handle in self._arrays:
            last_connect_x = self._arrays[array_handle]
        else:
            last_connect_x = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    self._handle,
                                    quippy._quippy.f90wrap_potential_minimise__array__last_connect_x)
            self._arrays[array_handle] = last_connect_x
        return last_connect_x
    
    @last_connect_x.setter
    def last_connect_x(self, last_connect_x):
        self.last_connect_x[...] = last_connect_x
    
    @property
    def minim_pot(self):
        """
        Element minim_pot ftype=type(potential) pytype=Potential
        
        
        Defined at Potential.fpp line 418
        
        """
        minim_pot_handle = quippy._quippy.f90wrap_potential_minimise__get__minim_pot(self._handle)
        if tuple(minim_pot_handle) in self._objs:
            minim_pot = self._objs[tuple(minim_pot_handle)]
        else:
            minim_pot = Potential.from_handle(minim_pot_handle)
            self._objs[tuple(minim_pot_handle)] = minim_pot
        return minim_pot
    
    @minim_pot.setter
    def minim_pot(self, minim_pot):
        minim_pot = minim_pot._handle
        quippy._quippy.f90wrap_potential_minimise__set__minim_pot(self._handle, minim_pot)
    
    @property
    def external_pressure(self):
        """
        Element external_pressure ftype=real(dp) pytype=float
        
        
        Defined at Potential.fpp line 420
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            quippy._quippy.f90wrap_potential_minimise__array__external_pressure(self._handle)
        if array_handle in self._arrays:
            external_pressure = self._arrays[array_handle]
        else:
            external_pressure = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    self._handle,
                                    quippy._quippy.f90wrap_potential_minimise__array__external_pressure)
            self._arrays[array_handle] = external_pressure
        return external_pressure
    
    @external_pressure.setter
    def external_pressure(self, external_pressure):
        self.external_pressure[...] = external_pressure
    
    @property
    def connectivity_rebuilt(self):
        """
        Element connectivity_rebuilt ftype=logical pytype=bool
        
        
        Defined at Potential.fpp line 421
        
        """
        return quippy._quippy.f90wrap_potential_minimise__get__connectivity_rebuilt(self._handle)
    
    @connectivity_rebuilt.setter
    def connectivity_rebuilt(self, connectivity_rebuilt):
        quippy._quippy.f90wrap_potential_minimise__set__connectivity_rebuilt(self._handle, connectivity_rebuilt)
    
    def __str__(self):
        ret = ['<potential_minimise>{\n']
        ret.append('    minim_pos_lat_preconditioner : ')
        ret.append(repr(self.minim_pos_lat_preconditioner))
        ret.append(',\n    minim_save_lat : ')
        ret.append(repr(self.minim_save_lat))
        ret.append(',\n    minim_args_str : ')
        ret.append(repr(self.minim_args_str))
        ret.append(',\n    minim_do_pos : ')
        ret.append(repr(self.minim_do_pos))
        ret.append(',\n    minim_do_lat : ')
        ret.append(repr(self.minim_do_lat))
        ret.append(',\n    minim_n_eval_e : ')
        ret.append(repr(self.minim_n_eval_e))
        ret.append(',\n    minim_n_eval_f : ')
        ret.append(repr(self.minim_n_eval_f))
        ret.append(',\n    minim_n_eval_ef : ')
        ret.append(repr(self.minim_n_eval_ef))
        ret.append(',\n    pos_lat_preconditioner_factor : ')
        ret.append(repr(self.pos_lat_preconditioner_factor))
        ret.append(',\n    minim_at : ')
        ret.append(repr(self.minim_at))
        ret.append(',\n    last_connect_x : ')
        ret.append(repr(self.last_connect_x))
        ret.append(',\n    minim_pot : ')
        ret.append(repr(self.minim_pot))
        ret.append(',\n    external_pressure : ')
        ret.append(repr(self.external_pressure))
        ret.append(',\n    connectivity_rebuilt : ')
        ret.append(repr(self.connectivity_rebuilt))
        ret.append('}')
        return ''.join(ret)
    
    _dt_array_initialisers = []
    

@f90wrap.runtime.register_class("quippy.Potential_Sum")
class Potential_Sum(f90wrap.runtime.FortranDerivedType):
    """
    Type(name=potential_sum)
    
    
    Defined at Potential.fpp lines 431-436
    
    """
    def __init__(self, args_str, pot1, pot2, error=None, handle=None):
        """
        self = Potential_Sum(args_str, pot1, pot2[, error])
        
        
        Defined at Potential.fpp lines 2118-2128
        
        Parameters
        ----------
        args_str : str
        pot1 : Potential
        pot2 : Potential
        error : int
        
        Returns
        -------
        this : Potential_Sum
        
        Potential type which abstracts all QUIP interatomic potentials
        
        Provides interface to all energy/force/virial calculating schemes,
        including actual calculations, as well as abstract hybrid schemes
        such as LOTF, Force Mixing, ONIOM, and the local energy scheme.
        
        Typically a Potential is constructed from an initialisation
        args_str and an XML parameter file, e.g. in Fortran::
        
        type(InOutput) :: xml_file
        type(Potential) :: pot
        ...
        call initialise(xml_file, 'SW.xml', INPUT)
        call initialise(pot, 'IP SW', param_file=xml_file)
        
        Or, equivaently in Python::
        
        pot = Potential('IP SW', param_filename='SW.xml')
        
        creates a Stillinger-Weber potential using the parameters from
        the file 'SW.xml'. The XML parameters can also be given directly
        as a string, via the `param_str` argument.
        
        The main workhorse is the :meth:`calc` routine, which is used
        internally to perform all calculations, e.g. to calculate forces::
        
        type(Atoms) :: at
        real(dp) :: force(3,8)
        ...
        call diamond(at, 5.44, 14)
        call randomise(at%pos, 0.01)
        call calc(pot, at, force=force)
        
        Note that there is now no need to set the 'Atoms%cutoff' attribute to the
        cutoff of this Potential: if it is less than this it will be increased
        automatically and a warning will be printed.
        The neighbour lists are updated automatically with the
        :meth:`~quippy.atoms.Atoms.calc_connect` routine. For efficiency,
        it's a good idea to set at%cutoff_skin greater than zero to decrease
        the frequency at which the connectivity needs to be rebuilt.
        
        A Potential can be used to optimise the geometry of an
        :class:`~quippy.atoms.Atoms` structure, using the :meth:`minim` routine,
        (or, in Python, via  the :class:`Minim` wrapper class).
        """
        f90wrap.runtime.FortranDerivedType.__init__(self)
        result = quippy._quippy.f90wrap_potential_sum_initialise(args_str=args_str, pot1=pot1._handle, pot2=pot2._handle, \
            error=error)
        self._handle = result[0] if isinstance(result, tuple) else result
    
    def __del__(self):
        """
        Destructor for class Potential_Sum
        
        
        Defined at Potential.fpp lines 2130-2133
        
        Parameters
        ----------
        this : Potential_Sum
        
        """
        if self._alloc:
            quippy._quippy.f90wrap_potential_sum_finalise(this=self._handle)
    
    def print(self, file=None, dict=None):
        """
        print(self[, file, dict])
        
        
        Defined at Potential.fpp lines 2135-2156
        
        Parameters
        ----------
        this : Potential_Sum
        file : Inoutput
        dict : Dictionary
        
        """
        quippy._quippy.f90wrap_potential_sum_print(this=self._handle, file=None if file is None else file._handle, dict=None if \
            dict is None else dict._handle)
    
    def cutoff(self):
        """
        potential_sum_cutoff = cutoff(self)
        
        
        Defined at Potential.fpp lines 2250-2257
        
        Parameters
        ----------
        this : Potential_Sum
        
        Returns
        -------
        potential_sum_cutoff : float
        
        Return the cutoff of this 'Potential', in Angstrom. This is the
        minimum neighbour connectivity cutoff that should be used: if
        you're doing MD you'll want to use a slightly larger cutoff so
        that new neighbours don't drift in to range between connectivity
        updates
        """
        potential_sum_cutoff = quippy._quippy.f90wrap_potential_sum_cutoff(this=self._handle)
        return potential_sum_cutoff
    
    def calc(self, at, args_str=None, error=None):
        """
        calc(self, at[, args_str, error])
        
        
        Defined at Potential.fpp lines 2158-2248
        
        Parameters
        ----------
        this : Potential_Sum
        at : Atoms
        args_str : str
        error : int
        
        Apply this Potential to the Atoms object
        'at'. Atoms%calc_connect is automatically called to update the
        connecticvity information -- if efficiency is important to you,
        ensure that at%cutoff_skin is set to a non-zero value to decrease
        the frequence of connectivity updates.
        optional arguments determine what should be calculated and how
        it will be returned. Each physical quantity has a
        corresponding optional argument, which can either be an 'True'
        to store the result inside the Atoms object(i.e. in
        Atoms%params' or in 'Atoms%properties' with the
        default name, a string to specify a different property or
        parameter name, or an array of the the correct shape to
        receive the quantity in question, as set out in the table
        below.
        
        ================  ============= ================ =========================
        Array argument    Quantity      Shape            Default storage location
        ================  ============= ================ =========================
        ``energy``        Energy        ``()``                  ``energy`` param
        ``local_energy``  Local energy  ``(at.n,)``      ``local_energy`` property
        ``force``         Force         ``(3,at.n)``     ``force`` property
        ``virial``        Virial tensor ``(3,3)``        ``virial`` param
        ``local_virial``  Local virial  ``(3,3,at.n)``   ``local_virial`` property
        ================  ============= ================ =========================
        
        The 'args_str' argument is an optional string  containing
        additional arguments which depend on the particular Potential
        being used.
        
        Not all Potentials support all of these quantities: an error
        will be raised if you ask for something that is not supported.
        
        .. rubric:: args_str options
        
        =================== ==== ===== ========================================================================
        Name                Type Value Doc                                                                     
        =================== ==== ===== ========================================================================
        energy              None       No help yet. This source file was $LastChangedBy$                       
        force               None       No help yet. This source file was $LastChangedBy$                       
        virial              None       No help yet. This source file was $LastChangedBy$                       
        local_energy        None       No help yet. This source file was $LastChangedBy$                       
        local_virial        None       No help yet. This source file was $LastChangedBy$                       
        calc_args_pot1      None       additional args_str to pass along to pot1                               
        calc_args_pot2      None       additional args_str to pass along to pot2                               
        store_contributions bool F     if true, store contributions to sum with _pot1 and _pot2 suffixes       
        =================== ==== ===== ========================================================================
        
        
        """
        quippy._quippy.f90wrap_potential_sum_calc(this=self._handle, at=at._handle, args_str=args_str, error=error)
    
    @property
    def pot1(self):
        """
        Element pot1 ftype=type(potential) pytype=Potential
        
        
        Defined at Potential.fpp line 433
        
        """
        pot1_handle = quippy._quippy.f90wrap_potential_sum__get__pot1(self._handle)
        if tuple(pot1_handle) in self._objs:
            pot1 = self._objs[tuple(pot1_handle)]
        else:
            pot1 = Potential.from_handle(pot1_handle)
            self._objs[tuple(pot1_handle)] = pot1
        return pot1
    
    @pot1.setter
    def pot1(self, pot1):
        pot1 = pot1._handle
        quippy._quippy.f90wrap_potential_sum__set__pot1(self._handle, pot1)
    
    @property
    def pot2(self):
        """
        Element pot2 ftype=type(potential) pytype=Potential
        
        
        Defined at Potential.fpp line 434
        
        """
        pot2_handle = quippy._quippy.f90wrap_potential_sum__get__pot2(self._handle)
        if tuple(pot2_handle) in self._objs:
            pot2 = self._objs[tuple(pot2_handle)]
        else:
            pot2 = Potential.from_handle(pot2_handle)
            self._objs[tuple(pot2_handle)] = pot2
        return pot2
    
    @pot2.setter
    def pot2(self, pot2):
        pot2 = pot2._handle
        quippy._quippy.f90wrap_potential_sum__set__pot2(self._handle, pot2)
    
    @property
    def subtract_pot1(self):
        """
        Element subtract_pot1 ftype=logical pytype=bool
        
        
        Defined at Potential.fpp line 435
        
        """
        return quippy._quippy.f90wrap_potential_sum__get__subtract_pot1(self._handle)
    
    @subtract_pot1.setter
    def subtract_pot1(self, subtract_pot1):
        quippy._quippy.f90wrap_potential_sum__set__subtract_pot1(self._handle, subtract_pot1)
    
    @property
    def subtract_pot2(self):
        """
        Element subtract_pot2 ftype=logical pytype=bool
        
        
        Defined at Potential.fpp line 436
        
        """
        return quippy._quippy.f90wrap_potential_sum__get__subtract_pot2(self._handle)
    
    @subtract_pot2.setter
    def subtract_pot2(self, subtract_pot2):
        quippy._quippy.f90wrap_potential_sum__set__subtract_pot2(self._handle, subtract_pot2)
    
    def __str__(self):
        ret = ['<potential_sum>{\n']
        ret.append('    pot1 : ')
        ret.append(repr(self.pot1))
        ret.append(',\n    pot2 : ')
        ret.append(repr(self.pot2))
        ret.append(',\n    subtract_pot1 : ')
        ret.append(repr(self.subtract_pot1))
        ret.append(',\n    subtract_pot2 : ')
        ret.append(repr(self.subtract_pot2))
        ret.append('}')
        return ''.join(ret)
    
    _dt_array_initialisers = []
    

@f90wrap.runtime.register_class("quippy.Potential_FM")
class Potential_FM(f90wrap.runtime.FortranDerivedType):
    """
    Type(name=potential_fm)
    
    
    Defined at Potential.fpp lines 491-547
    
    """
    def __init__(self, args_str, qmpot, mmpot=None, reference_bulk=None, error=None, handle=None):
        """
        self = Potential_Fm(args_str, qmpot[, mmpot, reference_bulk, error])
        
        
        Defined at Potential.fpp lines 2296-2414
        
        Parameters
        ----------
        args_str : str
        qmpot : Potential
        mmpot : Potential
        	if mmpot is not given, a zero potential is assumed, this is most useful in LOTF mode
        
        reference_bulk : Atoms
        error : int
        
        Returns
        -------
        this : Potential_Fm
        
        Potential type which abstracts all QUIP interatomic potentials
        
        Provides interface to all energy/force/virial calculating schemes,
        including actual calculations, as well as abstract hybrid schemes
        such as LOTF, Force Mixing, ONIOM, and the local energy scheme.
        
        Typically a Potential is constructed from an initialisation
        args_str and an XML parameter file, e.g. in Fortran::
        
        type(InOutput) :: xml_file
        type(Potential) :: pot
        ...
        call initialise(xml_file, 'SW.xml', INPUT)
        call initialise(pot, 'IP SW', param_file=xml_file)
        
        Or, equivaently in Python::
        
        pot = Potential('IP SW', param_filename='SW.xml')
        
        creates a Stillinger-Weber potential using the parameters from
        the file 'SW.xml'. The XML parameters can also be given directly
        as a string, via the `param_str` argument.
        
        The main workhorse is the :meth:`calc` routine, which is used
        internally to perform all calculations, e.g. to calculate forces::
        
        type(Atoms) :: at
        real(dp) :: force(3,8)
        ...
        call diamond(at, 5.44, 14)
        call randomise(at%pos, 0.01)
        call calc(pot, at, force=force)
        
        Note that there is now no need to set the 'Atoms%cutoff' attribute to the
        cutoff of this Potential: if it is less than this it will be increased
        automatically and a warning will be printed.
        The neighbour lists are updated automatically with the
        :meth:`~quippy.atoms.Atoms.calc_connect` routine. For efficiency,
        it's a good idea to set at%cutoff_skin greater than zero to decrease
        the frequency at which the connectivity needs to be rebuilt.
        
        A Potential can be used to optimise the geometry of an
        :class:`~quippy.atoms.Atoms` structure, using the :meth:`minim` routine,
        (or, in Python, via  the :class:`Minim` wrapper class).
        
        .. rubric:: args_str options
        
        =============================== ===== ================= ===============================================
        Name                            Type  Value             Doc                                            
        =============================== ===== ================= ===============================================
        run_suffix                      None                    No help yet. This source file was              
                                                                $LastChangedBy$                                
        minimise_mm                     bool  F                 No help yet. This source file was              
                                                                $LastChangedBy$                                
        calc_weights                    bool  T                 No help yet. This source file was              
                                                                $LastChangedBy$                                
        method                          None  conserve_momentum No help yet. This source file was              
                                                                $LastChangedBy$                                
        mm_reweight                     float 1.0               No help yet. This source file was              
                                                                $LastChangedBy$                                
        conserve_momentum_weight_method None  uniform           No help yet. This source file was              
                                                                $LastChangedBy$                                
        mm_args_str                     None                    No help yet. This source file was              
                                                                $LastChangedBy$                                
        qm_args_str                     None                    No help yet. This source file was              
                                                                $LastChangedBy$                                
        qm_little_clusters_buffer_hops  int   3                 No help yet. This source file was              
                                                                $LastChangedBy$                                
        use_buffer_for_fitting          bool  F                 No help yet. This source file was              
                                                                $LastChangedBy$                                
        fit_hops                        int   3                 No help yet. This source file was              
                                                                $LastChangedBy$                                
        add_cut_H_in_fitlist            bool  F                 No help yet. This source file was              
                                                                $LastChangedBy$                                
        randomise_buffer                bool  F                 No help yet. This source file was              
                                                                $LastChangedBy$                                
        save_forces                     bool  T                 No help yet. This source file was              
                                                                $LastChangedBy$                                
        lotf_spring_hops                int   2                 No help yet. This source file was              
                                                                $LastChangedBy$                                
        lotf_interp_order               None  linear            No help yet. This source file was              
                                                                $LastChangedBy$                                
        lotf_interp_space               bool  F                 No help yet. This source file was              
                                                                $LastChangedBy$                                
        lotf_nneighb_only               bool  T                 No help yet. This source file was              
                                                                $LastChangedBy$                                
        minim_mm_method                 None  cg                No help yet. This source file was              
                                                                $LastChangedBy$                                
        minim_mm_tol                    float 1e-6              No help yet. This source file was              
                                                                $LastChangedBy$                                
        minim_mm_eps_guess              float 1e-4              No help yet. This source file was              
                                                                $LastChangedBy$                                
        minim_mm_max_steps              int   1000              No help yet. This source file was              
                                                                $LastChangedBy$                                
        minim_mm_linminroutine          None  FAST_LINMIN       No help yet. This source file was              
                                                                $LastChangedBy$                                
        minim_mm_do_pos                 bool  T                 No help yet. This source file was              
                                                                $LastChangedBy$                                
        minim_mm_do_lat                 bool  F                 No help yet. This source file was              
                                                                $LastChangedBy$                                
        minim_mm_do_print               bool  F                 No help yet. This source file was              
                                                                $LastChangedBy$                                
        minim_mm_args_str               None                    No help yet. This source file was              
                                                                $LastChangedBy$                                
        minimise_bulk                   bool  F                 No help yet. This source file was              
                                                                $LastChangedBy$                                
        do_tb_defaults                  bool  F                 No help yet. This source file was              
                                                                $LastChangedBy$                                
        do_rescale_r                    bool  F                 No help yet. This source file was              
                                                                $LastChangedBy$                                
        do_rescale_E                    bool  F                 No help yet. This source file was              
                                                                $LastChangedBy$                                
        =============================== ===== ================= ===============================================
        
        
        """
        f90wrap.runtime.FortranDerivedType.__init__(self)
        result = quippy._quippy.f90wrap_potential_fm_initialise(args_str=args_str, qmpot=qmpot._handle, mmpot=(None if mmpot is \
            None else mmpot._handle), reference_bulk=(None if reference_bulk is None else reference_bulk._handle), error=error)
        self._handle = result[0] if isinstance(result, tuple) else result
    
    def __del__(self):
        """
        Destructor for class Potential_Fm
        
        
        Defined at Potential.fpp lines 2416-2422
        
        Parameters
        ----------
        this : Potential_Fm
        
        """
        if self._alloc:
            quippy._quippy.f90wrap_potential_fm_finalise(this=self._handle)
    
    def print(self, file=None):
        """
        print(self[, file])
        
        
        Defined at Potential.fpp lines 2424-2474
        
        Parameters
        ----------
        this : Potential_Fm
        file : Inoutput
        
        """
        quippy._quippy.f90wrap_potential_fm_print(this=self._handle, file=None if file is None else file._handle)
    
    def cutoff(self):
        """
        potential_fm_cutoff = cutoff(self)
        
        
        Defined at Potential.fpp lines 2902-2914
        
        Parameters
        ----------
        this : Potential_Fm
        
        Returns
        -------
        potential_fm_cutoff : float
        
        Return the cutoff of this 'Potential', in Angstrom. This is the
        minimum neighbour connectivity cutoff that should be used: if
        you're doing MD you'll want to use a slightly larger cutoff so
        that new neighbours don't drift in to range between connectivity
        updates
        """
        potential_fm_cutoff = quippy._quippy.f90wrap_potential_fm_cutoff(this=self._handle)
        return potential_fm_cutoff
    
    def calc(self, at, args_str=None, error=None):
        """
        calc(self, at[, args_str, error])
        
        
        Defined at Potential.fpp lines 2476-2900
        
        Parameters
        ----------
        this : Potential_Fm
        at : Atoms
        args_str : str
        error : int
        
        Apply this Potential to the Atoms object
        'at'. Atoms%calc_connect is automatically called to update the
        connecticvity information -- if efficiency is important to you,
        ensure that at%cutoff_skin is set to a non-zero value to decrease
        the frequence of connectivity updates.
        optional arguments determine what should be calculated and how
        it will be returned. Each physical quantity has a
        corresponding optional argument, which can either be an 'True'
        to store the result inside the Atoms object(i.e. in
        Atoms%params' or in 'Atoms%properties' with the
        default name, a string to specify a different property or
        parameter name, or an array of the the correct shape to
        receive the quantity in question, as set out in the table
        below.
        
        ================  ============= ================ =========================
        Array argument    Quantity      Shape            Default storage location
        ================  ============= ================ =========================
        ``energy``        Energy        ``()``                  ``energy`` param
        ``local_energy``  Local energy  ``(at.n,)``      ``local_energy`` property
        ``force``         Force         ``(3,at.n)``     ``force`` property
        ``virial``        Virial tensor ``(3,3)``        ``virial`` param
        ``local_virial``  Local virial  ``(3,3,at.n)``   ``local_virial`` property
        ================  ============= ================ =========================
        
        The 'args_str' argument is an optional string  containing
        additional arguments which depend on the particular Potential
        being used.
        
        Not all Potentials support all of these quantities: an error
        will be raised if you ask for something that is not supported.
        
        .. rubric:: args_str options
        
        =============================== ===== ======================================== ========================
        Name                            Type  Value                                    Doc                     
        =============================== ===== ======================================== ========================
        run_suffix                      None  ''//this%run_suffix                      No help yet. This       
                                                                                       source file was         
                                                                                       $LastChangedBy$         
        minimise_mm                     None  ''//this%minimise_mm                     No help yet. This       
                                                                                       source file was         
                                                                                       $LastChangedBy$         
        calc_weights                    None  ''//this%calc_weights                    No help yet. This       
                                                                                       source file was         
                                                                                       $LastChangedBy$         
        method                          None  this%method                              No help yet. This       
                                                                                       source file was         
                                                                                       $LastChangedBy$         
        mm_reweight                     None  ''//this%mm_reweight                     No help yet. This       
                                                                                       source file was         
                                                                                       $LastChangedBy$         
        conserve_momentum_weight_method None  ''//this%conserve_momentum_weight_method No help yet. This       
                                                                                       source file was         
                                                                                       $LastChangedBy$         
        mm_args_str                     None  this%mm_args_str                         No help yet. This       
                                                                                       source file was         
                                                                                       $LastChangedBy$         
        qm_args_str                     None  this%qm_args_str                         No help yet. This       
                                                                                       source file was         
                                                                                       $LastChangedBy$         
        qm_little_clusters_buffer_hops  None  ''//this%qm_little_clusters_buffer_hops  No help yet. This       
                                                                                       source file was         
                                                                                       $LastChangedBy$         
        use_buffer_for_fitting          None  ''//this%use_buffer_for_fitting          No help yet. This       
                                                                                       source file was         
                                                                                       $LastChangedBy$         
        fit_hops                        None  ''//this%fit_hops                        No help yet. This       
                                                                                       source file was         
                                                                                       $LastChangedBy$         
        add_cut_H_in_fitlist            None  ''//this%add_cut_H_in_fitlist            No help yet. This       
                                                                                       source file was         
                                                                                       $LastChangedBy$         
        randomise_buffer                None  ''//this%randomise_buffer                No help yet. This       
                                                                                       source file was         
                                                                                       $LastChangedBy$         
        save_forces                     None  ''//this%save_forces                     No help yet. This       
                                                                                       source file was         
                                                                                       $LastChangedBy$         
        lotf_spring_hops                None  ''//this%lotf_spring_hops                No help yet. This       
                                                                                       source file was         
                                                                                       $LastChangedBy$         
        lotf_interp_order               None  this%lotf_interp_order                   No help yet. This       
                                                                                       source file was         
                                                                                       $LastChangedBy$         
        lotf_interp_space               None  ''//this%lotf_interp_space               No help yet. This       
                                                                                       source file was         
                                                                                       $LastChangedBy$         
        lotf_nneighb_only               None  ''//this%lotf_nneighb_only               No help yet. This       
                                                                                       source file was         
                                                                                       $LastChangedBy$         
        minim_mm_method                 None  cg                                       No help yet. This       
                                                                                       source file was         
                                                                                       $LastChangedBy$         
        minim_mm_tol                    float 1e-6                                     No help yet. This       
                                                                                       source file was         
                                                                                       $LastChangedBy$         
        minim_mm_eps_guess              float 1e-4                                     No help yet. This       
                                                                                       source file was         
                                                                                       $LastChangedBy$         
        minim_mm_max_steps              int   1000                                     No help yet. This       
                                                                                       source file was         
                                                                                       $LastChangedBy$         
        minim_mm_linminroutine          None  FAST_LINMIN                              No help yet. This       
                                                                                       source file was         
                                                                                       $LastChangedBy$         
        minim_mm_do_pos                 bool  T                                        No help yet. This       
                                                                                       source file was         
                                                                                       $LastChangedBy$         
        minim_mm_do_lat                 bool  F                                        No help yet. This       
                                                                                       source file was         
                                                                                       $LastChangedBy$         
        minim_mm_do_print               bool  F                                        No help yet. This       
                                                                                       source file was         
                                                                                       $LastChangedBy$         
        minim_mm_args_str               None                                           No help yet. This       
                                                                                       source file was         
                                                                                       $LastChangedBy$         
        lotf_do_init                    bool  T                                        No help yet. This       
                                                                                       source file was         
                                                                                       $LastChangedBy$         
        lotf_do_map                     bool  F                                        No help yet. This       
                                                                                       source file was         
                                                                                       $LastChangedBy$         
        lotf_do_qm                      bool  T                                        No help yet. This       
                                                                                       source file was         
                                                                                       $LastChangedBy$         
        lotf_do_fit                     bool  T                                        No help yet. This       
                                                                                       source file was         
                                                                                       $LastChangedBy$         
        lotf_do_interp                  bool  F                                        No help yet. This       
                                                                                       source file was         
                                                                                       $LastChangedBy$         
        lotf_interp                     float 0.0                                      No help yet. This       
                                                                                       source file was         
                                                                                       $LastChangedBy$         
        energy                          None                                           No help yet. This       
                                                                                       source file was         
                                                                                       $LastChangedBy$         
        force                           None                                           No help yet. This       
                                                                                       source file was         
                                                                                       $LastChangedBy$         
        virial                          None                                           No help yet. This       
                                                                                       source file was         
                                                                                       $LastChangedBy$         
        local_energy                    None                                           No help yet. This       
                                                                                       source file was         
                                                                                       $LastChangedBy$         
        local_virial                    None                                           No help yet. This       
                                                                                       source file was         
                                                                                       $LastChangedBy$         
        =============================== ===== ======================================== ========================
        
        
        """
        quippy._quippy.f90wrap_potential_fm_calc(this=self._handle, at=at._handle, args_str=args_str, error=error)
    
    @property
    def mmpot(self):
        """
        Element mmpot ftype=type(potential) pytype=Potential
        
        
        Defined at Potential.fpp line 492
        
        """
        mmpot_handle = quippy._quippy.f90wrap_potential_fm__get__mmpot(self._handle)
        if tuple(mmpot_handle) in self._objs:
            mmpot = self._objs[tuple(mmpot_handle)]
        else:
            mmpot = Potential.from_handle(mmpot_handle)
            self._objs[tuple(mmpot_handle)] = mmpot
        return mmpot
    
    @mmpot.setter
    def mmpot(self, mmpot):
        mmpot = mmpot._handle
        quippy._quippy.f90wrap_potential_fm__set__mmpot(self._handle, mmpot)
    
    @property
    def qmpot(self):
        """
        Element qmpot ftype=type(potential) pytype=Potential
        
        
        Defined at Potential.fpp line 493
        
        """
        qmpot_handle = quippy._quippy.f90wrap_potential_fm__get__qmpot(self._handle)
        if tuple(qmpot_handle) in self._objs:
            qmpot = self._objs[tuple(qmpot_handle)]
        else:
            qmpot = Potential.from_handle(qmpot_handle)
            self._objs[tuple(qmpot_handle)] = qmpot
        return qmpot
    
    @qmpot.setter
    def qmpot(self, qmpot):
        qmpot = qmpot._handle
        quippy._quippy.f90wrap_potential_fm__set__qmpot(self._handle, qmpot)
    
    @property
    def init_args_str(self):
        """
        Element init_args_str ftype=character(string_length) pytype=str
        
        
        Defined at Potential.fpp line 495
        
        """
        return quippy._quippy.f90wrap_potential_fm__get__init_args_str(self._handle)
    
    @init_args_str.setter
    def init_args_str(self, init_args_str):
        quippy._quippy.f90wrap_potential_fm__set__init_args_str(self._handle, init_args_str)
    
    @property
    def minimise_mm(self):
        """
        Element minimise_mm ftype=logical pytype=bool
        
        
        Defined at Potential.fpp line 496
        
        Should classical degrees of freedom be minimised in each calc?
        """
        return quippy._quippy.f90wrap_potential_fm__get__minimise_mm(self._handle)
    
    @minimise_mm.setter
    def minimise_mm(self, minimise_mm):
        quippy._quippy.f90wrap_potential_fm__set__minimise_mm(self._handle, minimise_mm)
    
    @property
    def calc_weights(self):
        """
        Element calc_weights ftype=logical pytype=bool
        
        
        Defined at Potential.fpp line 497
        
        Should weights be recalculated on each call to 'calc()'
        """
        return quippy._quippy.f90wrap_potential_fm__get__calc_weights(self._handle)
    
    @calc_weights.setter
    def calc_weights(self, calc_weights):
        quippy._quippy.f90wrap_potential_fm__set__calc_weights(self._handle, calc_weights)
    
    @property
    def method(self):
        """
        Element method ftype=character(string_length) pytype=str
        
        
        Defined at Potential.fpp line 498
        
        What fit method to use. Options are:
        \begin{itemize}
        \item 'lotf_adj_pot_svd' --- LOTF using SVD to optimised the Adj Pot
        \item 'lotf_adj_pot_minim' --- LOTF using conjugate gradients to optimise the Adj Pot
        \item 'conserve_momentum' --- divide the total force on QM region over the fit atoms to conserve momentum
        \item 'force_mixing' --- force mixing with details depending on values of
        'buffer_hops', 'transtion_hops' and 'weight_interpolation'
        \item 'force_mixing_abrupt' --- simply use QM forces on QM atoms and MM forces on MM atoms
        (shorthand for 'method=force_mixing buffer_hops=0 transition_hops=0')
        \item 'force_mixing_smooth' --- use QM forces in QM region, MM forces in MM region and
        linearly interpolate in buffer region(shorthand for 'method=force_mixing weight_interpolation=hop_ramp')
        \item 'force_mixing_super_smooth' --- as above, but weight forces on each atom by distance from
        centre of mass of core region(shorthand for 'method=force_mixing weight_interpolation=distance_ramp')
        \end{itemize}
        Default method is 'conserve_momentum'.
        """
        return quippy._quippy.f90wrap_potential_fm__get__method(self._handle)
    
    @method.setter
    def method(self, method):
        quippy._quippy.f90wrap_potential_fm__set__method(self._handle, method)
    
    @property
    def run_suffix(self):
        """
        Element run_suffix ftype=character(string_length) pytype=str
        
        
        Defined at Potential.fpp line 513
        
        string to append to 'hybrid_mark' for actual hybrid_mark property
        """
        return quippy._quippy.f90wrap_potential_fm__get__run_suffix(self._handle)
    
    @run_suffix.setter
    def run_suffix(self, run_suffix):
        quippy._quippy.f90wrap_potential_fm__set__run_suffix(self._handle, run_suffix)
    
    @property
    def mm_reweight(self):
        """
        Element mm_reweight ftype=real(dp) pytype=float
        
        
        Defined at Potential.fpp line 514
        
        Factor by which to reweight classical forces in embed zone
        """
        return quippy._quippy.f90wrap_potential_fm__get__mm_reweight(self._handle)
    
    @mm_reweight.setter
    def mm_reweight(self, mm_reweight):
        quippy._quippy.f90wrap_potential_fm__set__mm_reweight(self._handle, mm_reweight)
    
    @property
    def conserve_momentum_weight_method(self):
        """
        Element conserve_momentum_weight_method ftype=character(string_length) pytype=str
        
        
        Defined at Potential.fpp line 515
        
        Weight method to use with 'method=conserve_momentum'. Should be one of
        'uniform' (default), 'mass', 'mass^2' or 'user',
        with the last referring to a 'conserve_momentum_weight'
        property in the Atoms object.
        """
        return quippy._quippy.f90wrap_potential_fm__get__conserve_momentum_weight_method(self._handle)
    
    @conserve_momentum_weight_method.setter
    def conserve_momentum_weight_method(self, conserve_momentum_weight_method):
        quippy._quippy.f90wrap_potential_fm__set__conserve_momentum_weight_method(self._handle, conserve_momentum_weight_method)
    
    @property
    def mm_args_str(self):
        """
        Element mm_args_str ftype=character(string_length) pytype=str
        
        
        Defined at Potential.fpp line 519
        
        Args string to be passed to 'calc' method of 'mmpot'
        """
        return quippy._quippy.f90wrap_potential_fm__get__mm_args_str(self._handle)
    
    @mm_args_str.setter
    def mm_args_str(self, mm_args_str):
        quippy._quippy.f90wrap_potential_fm__set__mm_args_str(self._handle, mm_args_str)
    
    @property
    def qm_args_str(self):
        """
        Element qm_args_str ftype=character(string_length) pytype=str
        
        
        Defined at Potential.fpp line 520
        
        Args string to be passed to 'calc' method of 'qmpot'
        """
        return quippy._quippy.f90wrap_potential_fm__get__qm_args_str(self._handle)
    
    @qm_args_str.setter
    def qm_args_str(self, qm_args_str):
        quippy._quippy.f90wrap_potential_fm__set__qm_args_str(self._handle, qm_args_str)
    
    @property
    def qm_little_clusters_buffer_hops(self):
        """
        Element qm_little_clusters_buffer_hops ftype=integer  pytype=int
        
        
        Defined at Potential.fpp line 521
        
        Number of bond hops used for buffer region for qm calcs with little clusters
        """
        return quippy._quippy.f90wrap_potential_fm__get__qm_little_clusters_buffer_hops(self._handle)
    
    @qm_little_clusters_buffer_hops.setter
    def qm_little_clusters_buffer_hops(self, qm_little_clusters_buffer_hops):
        quippy._quippy.f90wrap_potential_fm__set__qm_little_clusters_buffer_hops(self._handle, qm_little_clusters_buffer_hops)
    
    @property
    def use_buffer_for_fitting(self):
        """
        Element use_buffer_for_fitting ftype=logical pytype=bool
        
        
        Defined at Potential.fpp line 522
        
        Whether to generate the fit region or just use the buffer as the fit region. Only for method=conserve_momentum
        """
        return quippy._quippy.f90wrap_potential_fm__get__use_buffer_for_fitting(self._handle)
    
    @use_buffer_for_fitting.setter
    def use_buffer_for_fitting(self, use_buffer_for_fitting):
        quippy._quippy.f90wrap_potential_fm__set__use_buffer_for_fitting(self._handle, use_buffer_for_fitting)
    
    @property
    def fit_hops(self):
        """
        Element fit_hops ftype=integer  pytype=int
        
        
        Defined at Potential.fpp line 523
        
        Number of bond hops used for fit region. Applies to 'conserve_momentum' and 'lotf_*' methods only.
        """
        return quippy._quippy.f90wrap_potential_fm__get__fit_hops(self._handle)
    
    @fit_hops.setter
    def fit_hops(self, fit_hops):
        quippy._quippy.f90wrap_potential_fm__set__fit_hops(self._handle, fit_hops)
    
    @property
    def add_cut_h_in_fitlist(self):
        """
        Element add_cut_h_in_fitlist ftype=logical pytype=bool
        
        
        Defined at Potential.fpp line 524
        
        Whether to extend the fit region where a cut hydrogen is cut after the fitlist selection.
        This will ensure to only include whole water molecules in the fitlist.
        """
        return quippy._quippy.f90wrap_potential_fm__get__add_cut_h_in_fitlist(self._handle)
    
    @add_cut_h_in_fitlist.setter
    def add_cut_h_in_fitlist(self, add_cut_h_in_fitlist):
        quippy._quippy.f90wrap_potential_fm__set__add_cut_h_in_fitlist(self._handle, add_cut_h_in_fitlist)
    
    @property
    def randomise_buffer(self):
        """
        Element randomise_buffer ftype=logical pytype=bool
        
        
        Defined at Potential.fpp line 526
        
        If true, then positions of outer layer of buffer atoms will be randomised slightly. Default false.
        """
        return quippy._quippy.f90wrap_potential_fm__get__randomise_buffer(self._handle)
    
    @randomise_buffer.setter
    def randomise_buffer(self, randomise_buffer):
        quippy._quippy.f90wrap_potential_fm__set__randomise_buffer(self._handle, randomise_buffer)
    
    @property
    def save_forces(self):
        """
        Element save_forces ftype=logical pytype=bool
        
        
        Defined at Potential.fpp line 527
        
        If true, save MM, QM and total forces as properties in the Atoms object(default true)
        """
        return quippy._quippy.f90wrap_potential_fm__get__save_forces(self._handle)
    
    @save_forces.setter
    def save_forces(self, save_forces):
        quippy._quippy.f90wrap_potential_fm__set__save_forces(self._handle, save_forces)
    
    @property
    def lotf_spring_hops(self):
        """
        Element lotf_spring_hops ftype=integer  pytype=int
        
        
        Defined at Potential.fpp line 528
        
        Maximum lengths of springs for LOTF 'adj_pot_svd' and 'adj_pot_minim' methods(default is 2).
        """
        return quippy._quippy.f90wrap_potential_fm__get__lotf_spring_hops(self._handle)
    
    @lotf_spring_hops.setter
    def lotf_spring_hops(self, lotf_spring_hops):
        quippy._quippy.f90wrap_potential_fm__set__lotf_spring_hops(self._handle, lotf_spring_hops)
    
    @property
    def lotf_interp_order(self):
        """
        Element lotf_interp_order ftype=character(string_length) pytype=str
        
        
        Defined at Potential.fpp line 529
        
        Interpolation order: should be one of 'linear', 'quadratic', or 'cubic'. Default is 'linear'.
        """
        return quippy._quippy.f90wrap_potential_fm__get__lotf_interp_order(self._handle)
    
    @lotf_interp_order.setter
    def lotf_interp_order(self, lotf_interp_order):
        quippy._quippy.f90wrap_potential_fm__set__lotf_interp_order(self._handle, lotf_interp_order)
    
    @property
    def lotf_interp_space(self):
        """
        Element lotf_interp_space ftype=logical pytype=bool
        
        
        Defined at Potential.fpp line 530
        
        Do spatial rather than temporal interpolation of adj pot parameters. Default is false.
        """
        return quippy._quippy.f90wrap_potential_fm__get__lotf_interp_space(self._handle)
    
    @lotf_interp_space.setter
    def lotf_interp_space(self, lotf_interp_space):
        quippy._quippy.f90wrap_potential_fm__set__lotf_interp_space(self._handle, lotf_interp_space)
    
    @property
    def lotf_nneighb_only(self):
        """
        Element lotf_nneighb_only ftype=logical pytype=bool
        
        
        Defined at Potential.fpp line 531
        
        If true(which is the default), uses nearest neigbour hopping to determine fit atoms
        """
        return quippy._quippy.f90wrap_potential_fm__get__lotf_nneighb_only(self._handle)
    
    @lotf_nneighb_only.setter
    def lotf_nneighb_only(self, lotf_nneighb_only):
        quippy._quippy.f90wrap_potential_fm__set__lotf_nneighb_only(self._handle, lotf_nneighb_only)
    
    @property
    def do_rescale_r(self):
        """
        Element do_rescale_r ftype=logical pytype=bool
        
        
        Defined at Potential.fpp line 532
        
        If true rescale positions in QM region by r_scale_pot1
        """
        return quippy._quippy.f90wrap_potential_fm__get__do_rescale_r(self._handle)
    
    @do_rescale_r.setter
    def do_rescale_r(self, do_rescale_r):
        quippy._quippy.f90wrap_potential_fm__set__do_rescale_r(self._handle, do_rescale_r)
    
    @property
    def do_rescale_e(self):
        """
        Element do_rescale_e ftype=logical pytype=bool
        
        
        Defined at Potential.fpp line 533
        
        If true rescale energies in QM region by E_scale_pot1
        """
        return quippy._quippy.f90wrap_potential_fm__get__do_rescale_e(self._handle)
    
    @do_rescale_e.setter
    def do_rescale_e(self, do_rescale_e):
        quippy._quippy.f90wrap_potential_fm__set__do_rescale_e(self._handle, do_rescale_e)
    
    @property
    def r_scale_pot1(self):
        """
        Element r_scale_pot1 ftype=real(dp) pytype=float
        
        
        Defined at Potential.fpp line 534
        
        Rescale positions in QM region by this factor
        """
        return quippy._quippy.f90wrap_potential_fm__get__r_scale_pot1(self._handle)
    
    @r_scale_pot1.setter
    def r_scale_pot1(self, r_scale_pot1):
        quippy._quippy.f90wrap_potential_fm__set__r_scale_pot1(self._handle, r_scale_pot1)
    
    @property
    def e_scale_pot1(self):
        """
        Element e_scale_pot1 ftype=real(dp) pytype=float
        
        
        Defined at Potential.fpp line 535
        
        Rescale energy in QM region by this factor
        """
        return quippy._quippy.f90wrap_potential_fm__get__e_scale_pot1(self._handle)
    
    @e_scale_pot1.setter
    def e_scale_pot1(self, e_scale_pot1):
        quippy._quippy.f90wrap_potential_fm__set__e_scale_pot1(self._handle, e_scale_pot1)
    
    @property
    def minim_mm_method(self):
        """
        Element minim_mm_method ftype=character(string_length) pytype=str
        
        
        Defined at Potential.fpp line 536
        
        """
        return quippy._quippy.f90wrap_potential_fm__get__minim_mm_method(self._handle)
    
    @minim_mm_method.setter
    def minim_mm_method(self, minim_mm_method):
        quippy._quippy.f90wrap_potential_fm__set__minim_mm_method(self._handle, minim_mm_method)
    
    @property
    def minim_mm_tol(self):
        """
        Element minim_mm_tol ftype=real(dp) pytype=float
        
        
        Defined at Potential.fpp line 537
        
        """
        return quippy._quippy.f90wrap_potential_fm__get__minim_mm_tol(self._handle)
    
    @minim_mm_tol.setter
    def minim_mm_tol(self, minim_mm_tol):
        quippy._quippy.f90wrap_potential_fm__set__minim_mm_tol(self._handle, minim_mm_tol)
    
    @property
    def minim_mm_eps_guess(self):
        """
        Element minim_mm_eps_guess ftype=real(dp) pytype=float
        
        
        Defined at Potential.fpp line 537
        
        """
        return quippy._quippy.f90wrap_potential_fm__get__minim_mm_eps_guess(self._handle)
    
    @minim_mm_eps_guess.setter
    def minim_mm_eps_guess(self, minim_mm_eps_guess):
        quippy._quippy.f90wrap_potential_fm__set__minim_mm_eps_guess(self._handle, minim_mm_eps_guess)
    
    @property
    def minim_mm_max_steps(self):
        """
        Element minim_mm_max_steps ftype=integer        pytype=int
        
        
        Defined at Potential.fpp line 538
        
        """
        return quippy._quippy.f90wrap_potential_fm__get__minim_mm_max_steps(self._handle)
    
    @minim_mm_max_steps.setter
    def minim_mm_max_steps(self, minim_mm_max_steps):
        quippy._quippy.f90wrap_potential_fm__set__minim_mm_max_steps(self._handle, minim_mm_max_steps)
    
    @property
    def minim_mm_linminroutine(self):
        """
        Element minim_mm_linminroutine ftype=character(string_length) pytype=str
        
        
        Defined at Potential.fpp line 539
        
        """
        return quippy._quippy.f90wrap_potential_fm__get__minim_mm_linminroutine(self._handle)
    
    @minim_mm_linminroutine.setter
    def minim_mm_linminroutine(self, minim_mm_linminroutine):
        quippy._quippy.f90wrap_potential_fm__set__minim_mm_linminroutine(self._handle, minim_mm_linminroutine)
    
    @property
    def minim_mm_do_pos(self):
        """
        Element minim_mm_do_pos ftype=logical pytype=bool
        
        
        Defined at Potential.fpp line 540
        
        """
        return quippy._quippy.f90wrap_potential_fm__get__minim_mm_do_pos(self._handle)
    
    @minim_mm_do_pos.setter
    def minim_mm_do_pos(self, minim_mm_do_pos):
        quippy._quippy.f90wrap_potential_fm__set__minim_mm_do_pos(self._handle, minim_mm_do_pos)
    
    @property
    def minim_mm_do_lat(self):
        """
        Element minim_mm_do_lat ftype=logical pytype=bool
        
        
        Defined at Potential.fpp line 540
        
        """
        return quippy._quippy.f90wrap_potential_fm__get__minim_mm_do_lat(self._handle)
    
    @minim_mm_do_lat.setter
    def minim_mm_do_lat(self, minim_mm_do_lat):
        quippy._quippy.f90wrap_potential_fm__set__minim_mm_do_lat(self._handle, minim_mm_do_lat)
    
    @property
    def minim_mm_do_print(self):
        """
        Element minim_mm_do_print ftype=logical pytype=bool
        
        
        Defined at Potential.fpp line 541
        
        """
        return quippy._quippy.f90wrap_potential_fm__get__minim_mm_do_print(self._handle)
    
    @minim_mm_do_print.setter
    def minim_mm_do_print(self, minim_mm_do_print):
        quippy._quippy.f90wrap_potential_fm__set__minim_mm_do_print(self._handle, minim_mm_do_print)
    
    @property
    def minim_mm_args_str(self):
        """
        Element minim_mm_args_str ftype=character(string_length) pytype=str
        
        
        Defined at Potential.fpp line 542
        
        """
        return quippy._quippy.f90wrap_potential_fm__get__minim_mm_args_str(self._handle)
    
    @minim_mm_args_str.setter
    def minim_mm_args_str(self, minim_mm_args_str):
        quippy._quippy.f90wrap_potential_fm__set__minim_mm_args_str(self._handle, minim_mm_args_str)
    
    @property
    def create_hybrid_weights_params(self):
        """
        Element create_hybrid_weights_params ftype=type(dictionary) pytype=Dictionary
        
        
        Defined at Potential.fpp line 543
        
        extra arguments to pass create_hybrid_weights
        """
        create_hybrid_weights_params_handle = \
            quippy._quippy.f90wrap_potential_fm__get__create_hybrid_weights_params(self._handle)
        if tuple(create_hybrid_weights_params_handle) in self._objs:
            create_hybrid_weights_params = self._objs[tuple(create_hybrid_weights_params_handle)]
        else:
            create_hybrid_weights_params = Dictionary.from_handle(create_hybrid_weights_params_handle)
            self._objs[tuple(create_hybrid_weights_params_handle)] = create_hybrid_weights_params
        return create_hybrid_weights_params
    
    @create_hybrid_weights_params.setter
    def create_hybrid_weights_params(self, create_hybrid_weights_params):
        create_hybrid_weights_params = create_hybrid_weights_params._handle
        quippy._quippy.f90wrap_potential_fm__set__create_hybrid_weights_params(self._handle, create_hybrid_weights_params)
    
    @property
    def relax_pot(self):
        """
        Element relax_pot ftype=type(potential) pytype=Potential
        
        
        Defined at Potential.fpp line 544
        
        """
        relax_pot_handle = quippy._quippy.f90wrap_potential_fm__get__relax_pot(self._handle)
        if tuple(relax_pot_handle) in self._objs:
            relax_pot = self._objs[tuple(relax_pot_handle)]
        else:
            relax_pot = Potential.from_handle(relax_pot_handle)
            self._objs[tuple(relax_pot_handle)] = relax_pot
        return relax_pot
    
    @relax_pot.setter
    def relax_pot(self, relax_pot):
        relax_pot = relax_pot._handle
        quippy._quippy.f90wrap_potential_fm__set__relax_pot(self._handle, relax_pot)
    
    @property
    def minim_inoutput_movie(self):
        """
        Element minim_inoutput_movie ftype=type(inoutput) pytype=Inoutput
        
        
        Defined at Potential.fpp line 545
        
        """
        minim_inoutput_movie_handle = quippy._quippy.f90wrap_potential_fm__get__minim_inoutput_movie(self._handle)
        if tuple(minim_inoutput_movie_handle) in self._objs:
            minim_inoutput_movie = self._objs[tuple(minim_inoutput_movie_handle)]
        else:
            minim_inoutput_movie = InOutput.from_handle(minim_inoutput_movie_handle)
            self._objs[tuple(minim_inoutput_movie_handle)] = minim_inoutput_movie
        return minim_inoutput_movie
    
    @minim_inoutput_movie.setter
    def minim_inoutput_movie(self, minim_inoutput_movie):
        minim_inoutput_movie = minim_inoutput_movie._handle
        quippy._quippy.f90wrap_potential_fm__set__minim_inoutput_movie(self._handle, minim_inoutput_movie)
    
    def __str__(self):
        ret = ['<potential_fm>{\n']
        ret.append('    mmpot : ')
        ret.append(repr(self.mmpot))
        ret.append(',\n    qmpot : ')
        ret.append(repr(self.qmpot))
        ret.append(',\n    init_args_str : ')
        ret.append(repr(self.init_args_str))
        ret.append(',\n    minimise_mm : ')
        ret.append(repr(self.minimise_mm))
        ret.append(',\n    calc_weights : ')
        ret.append(repr(self.calc_weights))
        ret.append(',\n    method : ')
        ret.append(repr(self.method))
        ret.append(',\n    run_suffix : ')
        ret.append(repr(self.run_suffix))
        ret.append(',\n    mm_reweight : ')
        ret.append(repr(self.mm_reweight))
        ret.append(',\n    conserve_momentum_weight_method : ')
        ret.append(repr(self.conserve_momentum_weight_method))
        ret.append(',\n    mm_args_str : ')
        ret.append(repr(self.mm_args_str))
        ret.append(',\n    qm_args_str : ')
        ret.append(repr(self.qm_args_str))
        ret.append(',\n    qm_little_clusters_buffer_hops : ')
        ret.append(repr(self.qm_little_clusters_buffer_hops))
        ret.append(',\n    use_buffer_for_fitting : ')
        ret.append(repr(self.use_buffer_for_fitting))
        ret.append(',\n    fit_hops : ')
        ret.append(repr(self.fit_hops))
        ret.append(',\n    add_cut_h_in_fitlist : ')
        ret.append(repr(self.add_cut_h_in_fitlist))
        ret.append(',\n    randomise_buffer : ')
        ret.append(repr(self.randomise_buffer))
        ret.append(',\n    save_forces : ')
        ret.append(repr(self.save_forces))
        ret.append(',\n    lotf_spring_hops : ')
        ret.append(repr(self.lotf_spring_hops))
        ret.append(',\n    lotf_interp_order : ')
        ret.append(repr(self.lotf_interp_order))
        ret.append(',\n    lotf_interp_space : ')
        ret.append(repr(self.lotf_interp_space))
        ret.append(',\n    lotf_nneighb_only : ')
        ret.append(repr(self.lotf_nneighb_only))
        ret.append(',\n    do_rescale_r : ')
        ret.append(repr(self.do_rescale_r))
        ret.append(',\n    do_rescale_e : ')
        ret.append(repr(self.do_rescale_e))
        ret.append(',\n    r_scale_pot1 : ')
        ret.append(repr(self.r_scale_pot1))
        ret.append(',\n    e_scale_pot1 : ')
        ret.append(repr(self.e_scale_pot1))
        ret.append(',\n    minim_mm_method : ')
        ret.append(repr(self.minim_mm_method))
        ret.append(',\n    minim_mm_tol : ')
        ret.append(repr(self.minim_mm_tol))
        ret.append(',\n    minim_mm_eps_guess : ')
        ret.append(repr(self.minim_mm_eps_guess))
        ret.append(',\n    minim_mm_max_steps : ')
        ret.append(repr(self.minim_mm_max_steps))
        ret.append(',\n    minim_mm_linminroutine : ')
        ret.append(repr(self.minim_mm_linminroutine))
        ret.append(',\n    minim_mm_do_pos : ')
        ret.append(repr(self.minim_mm_do_pos))
        ret.append(',\n    minim_mm_do_lat : ')
        ret.append(repr(self.minim_mm_do_lat))
        ret.append(',\n    minim_mm_do_print : ')
        ret.append(repr(self.minim_mm_do_print))
        ret.append(',\n    minim_mm_args_str : ')
        ret.append(repr(self.minim_mm_args_str))
        ret.append(',\n    create_hybrid_weights_params : ')
        ret.append(repr(self.create_hybrid_weights_params))
        ret.append(',\n    relax_pot : ')
        ret.append(repr(self.relax_pot))
        ret.append(',\n    minim_inoutput_movie : ')
        ret.append(repr(self.minim_inoutput_movie))
        ret.append('}')
        return ''.join(ret)
    
    _dt_array_initialisers = []
    

@f90wrap.runtime.register_class("quippy.Potential_EVB")
class Potential_EVB(f90wrap.runtime.FortranDerivedType):
    """
    Type(name=potential_evb)
    
    
    Defined at Potential.fpp lines 567-581
    
    """
    def __init__(self, args_str, pot1, error=None, handle=None):
        """
        self = Potential_Evb(args_str, pot1[, error])
        
        
        Defined at Potential.fpp lines 2923-2951
        
        Parameters
        ----------
        args_str : str
        pot1 : Potential
        error : int
        
        Returns
        -------
        this : Potential_Evb
        
        Potential type which abstracts all QUIP interatomic potentials
        
        Provides interface to all energy/force/virial calculating schemes,
        including actual calculations, as well as abstract hybrid schemes
        such as LOTF, Force Mixing, ONIOM, and the local energy scheme.
        
        Typically a Potential is constructed from an initialisation
        args_str and an XML parameter file, e.g. in Fortran::
        
        type(InOutput) :: xml_file
        type(Potential) :: pot
        ...
        call initialise(xml_file, 'SW.xml', INPUT)
        call initialise(pot, 'IP SW', param_file=xml_file)
        
        Or, equivaently in Python::
        
        pot = Potential('IP SW', param_filename='SW.xml')
        
        creates a Stillinger-Weber potential using the parameters from
        the file 'SW.xml'. The XML parameters can also be given directly
        as a string, via the `param_str` argument.
        
        The main workhorse is the :meth:`calc` routine, which is used
        internally to perform all calculations, e.g. to calculate forces::
        
        type(Atoms) :: at
        real(dp) :: force(3,8)
        ...
        call diamond(at, 5.44, 14)
        call randomise(at%pos, 0.01)
        call calc(pot, at, force=force)
        
        Note that there is now no need to set the 'Atoms%cutoff' attribute to the
        cutoff of this Potential: if it is less than this it will be increased
        automatically and a warning will be printed.
        The neighbour lists are updated automatically with the
        :meth:`~quippy.atoms.Atoms.calc_connect` routine. For efficiency,
        it's a good idea to set at%cutoff_skin greater than zero to decrease
        the frequency at which the connectivity needs to be rebuilt.
        
        A Potential can be used to optimise the geometry of an
        :class:`~quippy.atoms.Atoms` structure, using the :meth:`minim` routine,
        (or, in Python, via  the :class:`Minim` wrapper class).
        
        .. rubric:: args_str options
        
        ======================= ===== ===== ===================================================================
        Name                    Type  Value Doc                                                                
        ======================= ===== ===== ===================================================================
        mm_args_str             None        Argumentum string to be passed on to the underlying MM             
                                            potential(s) of the EVB method.                                    
        topology_suffix1        None  _EVB1 Suffix of the first topology file of the EVB method.               
        topology_suffix2        None  _EVB2 Suffix of the second topology file of the EVB method.              
        form_bond               None  0 0   Which bond to form in the first topology and break in the second   
                                            topology used in the EVB calculation.                              
        break_bond              None  0 0   Which bond to break in the first topology and form in the second   
                                            topology used in the EVB calculation.                              
        diagonal_dE2            float 0.0   Energy offset between the energy minima of the two topologies of   
                                            the EVB method.                                                    
        offdiagonal_A12         float 0.0   A12 parameter of the coupling term                                 
                                            A12*exp(-mu12*r0-mu12_square*r0**2.0).                             
        offdiagonal_mu12        float 0.0   mu12 parameter of the coupling term                                
                                            A12*exp(-mu12*r0-mu12_square*r0**2.0).                             
        offdiagonal_mu12_square float 0.0   mu12_square parameter of the coupling parameter                    
                                            A12*exp(-mu12*r0-mu12_square*r0**2.0).                             
        offdiagonal_r0          float 0.0   r0 parameter of the coupling term                                  
                                            A12*exp(-mu12*r0-mu12_square*r0**2.0).                             
        save_forces             bool  T     Whether to save forces in atoms%params as EVB1_$forces$            
                                            EVB2_$forces$ if $forces$ is given when calling calc.              
        save_energies           bool  T     Whether to save energies in atoms%params as EVB1_$energy$ and      
                                            EVB2_$energy$ if $energy$ is given when calling calc.              
        ======================= ===== ===== ===================================================================
        
        
        """
        f90wrap.runtime.FortranDerivedType.__init__(self)
        result = quippy._quippy.f90wrap_potential_evb_initialise(args_str=args_str, pot1=pot1._handle, error=error)
        self._handle = result[0] if isinstance(result, tuple) else result
    
    def __del__(self):
        """
        Destructor for class Potential_Evb
        
        
        Defined at Potential.fpp lines 2953-2967
        
        Parameters
        ----------
        this : Potential_Evb
        
        """
        if self._alloc:
            quippy._quippy.f90wrap_potential_evb_finalise(this=self._handle)
    
    def print(self, file=None):
        """
        print(self[, file])
        
        
        Defined at Potential.fpp lines 2969-2995
        
        Parameters
        ----------
        this : Potential_Evb
        file : Inoutput
        
        """
        quippy._quippy.f90wrap_potential_evb_print(this=self._handle, file=None if file is None else file._handle)
    
    def cutoff(self):
        """
        potential_evb_cutoff = cutoff(self)
        
        
        Defined at Potential.fpp lines 3257-3264
        
        Parameters
        ----------
        this : Potential_Evb
        
        Returns
        -------
        potential_evb_cutoff : float
        
        Return the cutoff of this 'Potential', in Angstrom. This is the
        minimum neighbour connectivity cutoff that should be used: if
        you're doing MD you'll want to use a slightly larger cutoff so
        that new neighbours don't drift in to range between connectivity
        updates
        """
        potential_evb_cutoff = quippy._quippy.f90wrap_potential_evb_cutoff(this=self._handle)
        return potential_evb_cutoff
    
    def calc(self, at, args_str=None, error=None):
        """
        calc(self, at[, args_str, error])
        
        
        Defined at Potential.fpp lines 2997-3255
        
        Parameters
        ----------
        this : Potential_Evb
        at : Atoms
        args_str : str
        error : int
        
        Apply this Potential to the Atoms object
        'at'. Atoms%calc_connect is automatically called to update the
        connecticvity information -- if efficiency is important to you,
        ensure that at%cutoff_skin is set to a non-zero value to decrease
        the frequence of connectivity updates.
        optional arguments determine what should be calculated and how
        it will be returned. Each physical quantity has a
        corresponding optional argument, which can either be an 'True'
        to store the result inside the Atoms object(i.e. in
        Atoms%params' or in 'Atoms%properties' with the
        default name, a string to specify a different property or
        parameter name, or an array of the the correct shape to
        receive the quantity in question, as set out in the table
        below.
        
        ================  ============= ================ =========================
        Array argument    Quantity      Shape            Default storage location
        ================  ============= ================ =========================
        ``energy``        Energy        ``()``                  ``energy`` param
        ``local_energy``  Local energy  ``(at.n,)``      ``local_energy`` property
        ``force``         Force         ``(3,at.n)``     ``force`` property
        ``virial``        Virial tensor ``(3,3)``        ``virial`` param
        ``local_virial``  Local virial  ``(3,3,at.n)``   ``local_virial`` property
        ================  ============= ================ =========================
        
        The 'args_str' argument is an optional string  containing
        additional arguments which depend on the particular Potential
        being used.
        
        Not all Potentials support all of these quantities: an error
        will be raised if you ask for something that is not supported.
        
        .. rubric:: args_str options
        
        ======================= ==== ================================ =========================================
        Name                    Type Value                            Doc                                      
        ======================= ==== ================================ =========================================
        mm_args_str             None ''//this%mm_args_str             Argumentum string to be passed on to the 
                                                                      underlying MM potential(s) of the EVB    
                                                                      method.                                  
        topology_suffix1        None ''//this%topology_suffix1        Suffix of the first topology file of the 
                                                                      EVB method.                              
        topology_suffix2        None ''//this%topology_suffix2        Suffix of the second topology file of    
                                                                      the EVB method.                          
        form_bond               None ''//this%form_bond               Which bond to form in the first topology 
                                                                      and break in the second topology used in 
                                                                      the EVB calculation.                     
        break_bond              None ''//this%break_bond              Which bond to break in the first         
                                                                      topology and form in the second topology 
                                                                      used in the EVB calculation.             
        diagonal_dE2            None ''//this%diagonal_dE2            Energy offset between the energy minima  
                                                                      of the two topologies of the EVB method. 
        offdiagonal_A12         None ''//this%offdiagonal_A12         A12 parameter of the coupling term       
                                                                      A12*exp(-mu12*r0-mu12_square*r0**2.0).   
        offdiagonal_mu12        None ''//this%offdiagonal_mu12        mu12 parameter of the coupling term      
                                                                      A12*exp(-mu12*r0-mu12_square*r0**2.0).   
        offdiagonal_mu12_square None ''//this%offdiagonal_mu12_square mu12_square parameter of the coupling    
                                                                      term                                     
                                                                      A12*exp(-mu12*r0-mu12_square*r0**2.0).   
        offdiagonal_r0          None ''//this%offdiagonal_r0          r0 parameter of the coupling term        
                                                                      A12*exp(-mu12*r0-mu12_square*r0**2.0).   
        save_forces             None ''//this%save_forces             Whether to save forces in atoms%params   
                                                                      as EVB1_$forces$ EVB2_$forces$ if        
                                                                      $forces$ is given when calling calc.     
        save_energies           None ''//this%save_energies           Whether to save energies in atoms%params 
                                                                      as EVB1_$energy$ and EVB2_$energy$ if    
                                                                      $energy$ is given when calling calc.     
        energy                  None                                  Under what name to save the EVB          
                                                                      energies(EVB1_$energy$ and               
                                                                      EVB2_$energy$) in atoms%params.          
        force                   None                                  Under what name to save the EVB          
                                                                      forces(EVB1_$force$ and EVB2_$force$) in 
                                                                      atoms%data.                              
        virial                  None                                  Whether to calculate virial. This option 
                                                                      is not supported in EVB calculations.$   
        local_energy            None                                  Whether to calculate local energy. This  
                                                                      option is not supported in EVB           
                                                                      calculations.                            
        local_virial            None                                  Whether to calculate local virial. This  
                                                                      option is not supported in EVB           
                                                                      calculations.                            
        EVB_gap                 None                                  Under what name to save the EVB gap      
                                                                      energy in atoms%params. Forces on the    
                                                                      gap energy will be saved in              
                                                                      $EVB_gap$_force property.                
        ======================= ==== ================================ =========================================
        
        
        """
        quippy._quippy.f90wrap_potential_evb_calc(this=self._handle, at=at._handle, args_str=args_str, error=error)
    
    @property
    def pot1(self):
        """
        Element pot1 ftype=type(potential) pytype=Potential
        
        
        Defined at Potential.fpp line 569
        
        The underlying MM potential, pot1 and pot2
        """
        pot1_handle = quippy._quippy.f90wrap_potential_evb__get__pot1(self._handle)
        if tuple(pot1_handle) in self._objs:
            pot1 = self._objs[tuple(pot1_handle)]
        else:
            pot1 = Potential.from_handle(pot1_handle)
            self._objs[tuple(pot1_handle)] = pot1
        return pot1
    
    @pot1.setter
    def pot1(self, pot1):
        pot1 = pot1._handle
        quippy._quippy.f90wrap_potential_evb__set__pot1(self._handle, pot1)
    
    @property
    def mm_args_str(self):
        """
        Element mm_args_str ftype=character(string_length) pytype=str
        
        
        Defined at Potential.fpp line 570
        
        Args string to be passed to 'calc' method of pot1 and pot2
        """
        return quippy._quippy.f90wrap_potential_evb__get__mm_args_str(self._handle)
    
    @mm_args_str.setter
    def mm_args_str(self, mm_args_str):
        quippy._quippy.f90wrap_potential_evb__set__mm_args_str(self._handle, mm_args_str)
    
    @property
    def topology_suffix1(self):
        """
        Element topology_suffix1 ftype=character(string_length) pytype=str
        
        
        Defined at Potential.fpp line 571
        
        Suffix in topology filename, to be added to mm_args_str of pot1
        """
        return quippy._quippy.f90wrap_potential_evb__get__topology_suffix1(self._handle)
    
    @topology_suffix1.setter
    def topology_suffix1(self, topology_suffix1):
        quippy._quippy.f90wrap_potential_evb__set__topology_suffix1(self._handle, topology_suffix1)
    
    @property
    def topology_suffix2(self):
        """
        Element topology_suffix2 ftype=character(string_length) pytype=str
        
        
        Defined at Potential.fpp line 572
        
        Suffix in topology filename, to be added to mm_args_str of pot2
        """
        return quippy._quippy.f90wrap_potential_evb__get__topology_suffix2(self._handle)
    
    @topology_suffix2.setter
    def topology_suffix2(self, topology_suffix2):
        quippy._quippy.f90wrap_potential_evb__set__topology_suffix2(self._handle, topology_suffix2)
    
    @property
    def form_bond(self):
        """
        Element form_bond ftype=integer  pytype=int
        
        
        Defined at Potential.fpp line 573
        
        Atom pair that is bonded in EVB1 only
        """
        array_ndim, array_type, array_shape, array_handle = quippy._quippy.f90wrap_potential_evb__array__form_bond(self._handle)
        if array_handle in self._arrays:
            form_bond = self._arrays[array_handle]
        else:
            form_bond = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    self._handle,
                                    quippy._quippy.f90wrap_potential_evb__array__form_bond)
            self._arrays[array_handle] = form_bond
        return form_bond
    
    @form_bond.setter
    def form_bond(self, form_bond):
        self.form_bond[...] = form_bond
    
    @property
    def break_bond(self):
        """
        Element break_bond ftype=integer  pytype=int
        
        
        Defined at Potential.fpp line 574
        
        Atom pair that is bonded in EVB2 only
        """
        array_ndim, array_type, array_shape, array_handle = \
            quippy._quippy.f90wrap_potential_evb__array__break_bond(self._handle)
        if array_handle in self._arrays:
            break_bond = self._arrays[array_handle]
        else:
            break_bond = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    self._handle,
                                    quippy._quippy.f90wrap_potential_evb__array__break_bond)
            self._arrays[array_handle] = break_bond
        return break_bond
    
    @break_bond.setter
    def break_bond(self, break_bond):
        self.break_bond[...] = break_bond
    
    @property
    def diagonal_de2(self):
        """
        Element diagonal_de2 ftype=real(dp) pytype=float
        
        
        Defined at Potential.fpp line 575
        
        The energy offset to E2
        """
        return quippy._quippy.f90wrap_potential_evb__get__diagonal_de2(self._handle)
    
    @diagonal_de2.setter
    def diagonal_de2(self, diagonal_de2):
        quippy._quippy.f90wrap_potential_evb__set__diagonal_de2(self._handle, diagonal_de2)
    
    @property
    def offdiagonal_a12(self):
        """
        Element offdiagonal_a12 ftype=real(dp) pytype=float
        
        
        Defined at Potential.fpp line 576
        
        The offdiagonal pre-exponent factor of EVB Hamiltonian
        """
        return quippy._quippy.f90wrap_potential_evb__get__offdiagonal_a12(self._handle)
    
    @offdiagonal_a12.setter
    def offdiagonal_a12(self, offdiagonal_a12):
        quippy._quippy.f90wrap_potential_evb__set__offdiagonal_a12(self._handle, offdiagonal_a12)
    
    @property
    def offdiagonal_mu12(self):
        """
        Element offdiagonal_mu12 ftype=real(dp) pytype=float
        
        
        Defined at Potential.fpp line 577
        
        The offdiagonal exponent factor of the EVB Hamiltonian
        """
        return quippy._quippy.f90wrap_potential_evb__get__offdiagonal_mu12(self._handle)
    
    @offdiagonal_mu12.setter
    def offdiagonal_mu12(self, offdiagonal_mu12):
        quippy._quippy.f90wrap_potential_evb__set__offdiagonal_mu12(self._handle, offdiagonal_mu12)
    
    @property
    def offdiagonal_mu12_square(self):
        """
        Element offdiagonal_mu12_square ftype=real(dp) pytype=float
        
        
        Defined at Potential.fpp line 578
        
        The offdiagonal exponent factor of the EVB Hamiltonian:  A exp(-mu12(r-r0)-mu12_square(r-r0)^2)
        """
        return quippy._quippy.f90wrap_potential_evb__get__offdiagonal_mu12_square(self._handle)
    
    @offdiagonal_mu12_square.setter
    def offdiagonal_mu12_square(self, offdiagonal_mu12_square):
        quippy._quippy.f90wrap_potential_evb__set__offdiagonal_mu12_square(self._handle, offdiagonal_mu12_square)
    
    @property
    def offdiagonal_r0(self):
        """
        Element offdiagonal_r0 ftype=real(dp) pytype=float
        
        
        Defined at Potential.fpp line 579
        
        The offdiagonal exponent of the EVB Hamiltonian
        """
        return quippy._quippy.f90wrap_potential_evb__get__offdiagonal_r0(self._handle)
    
    @offdiagonal_r0.setter
    def offdiagonal_r0(self, offdiagonal_r0):
        quippy._quippy.f90wrap_potential_evb__set__offdiagonal_r0(self._handle, offdiagonal_r0)
    
    @property
    def save_forces(self):
        """
        Element save_forces ftype=logical pytype=bool
        
        
        Defined at Potential.fpp line 580
        
        Whether to save forces from the 2 MM calculations in the Atoms object(needed for force on E_GAP)
        """
        return quippy._quippy.f90wrap_potential_evb__get__save_forces(self._handle)
    
    @save_forces.setter
    def save_forces(self, save_forces):
        quippy._quippy.f90wrap_potential_evb__set__save_forces(self._handle, save_forces)
    
    @property
    def save_energies(self):
        """
        Element save_energies ftype=logical pytype=bool
        
        
        Defined at Potential.fpp line 581
        
        Whether to save energies from the 2 MM calculations in the Atoms object(needed for E_GAP)
        """
        return quippy._quippy.f90wrap_potential_evb__get__save_energies(self._handle)
    
    @save_energies.setter
    def save_energies(self, save_energies):
        quippy._quippy.f90wrap_potential_evb__set__save_energies(self._handle, save_energies)
    
    def __str__(self):
        ret = ['<potential_evb>{\n']
        ret.append('    pot1 : ')
        ret.append(repr(self.pot1))
        ret.append(',\n    mm_args_str : ')
        ret.append(repr(self.mm_args_str))
        ret.append(',\n    topology_suffix1 : ')
        ret.append(repr(self.topology_suffix1))
        ret.append(',\n    topology_suffix2 : ')
        ret.append(repr(self.topology_suffix2))
        ret.append(',\n    form_bond : ')
        ret.append(repr(self.form_bond))
        ret.append(',\n    break_bond : ')
        ret.append(repr(self.break_bond))
        ret.append(',\n    diagonal_de2 : ')
        ret.append(repr(self.diagonal_de2))
        ret.append(',\n    offdiagonal_a12 : ')
        ret.append(repr(self.offdiagonal_a12))
        ret.append(',\n    offdiagonal_mu12 : ')
        ret.append(repr(self.offdiagonal_mu12))
        ret.append(',\n    offdiagonal_mu12_square : ')
        ret.append(repr(self.offdiagonal_mu12_square))
        ret.append(',\n    offdiagonal_r0 : ')
        ret.append(repr(self.offdiagonal_r0))
        ret.append(',\n    save_forces : ')
        ret.append(repr(self.save_forces))
        ret.append(',\n    save_energies : ')
        ret.append(repr(self.save_energies))
        ret.append('}')
        return ''.join(ret)
    
    _dt_array_initialisers = []
    

@f90wrap.runtime.register_class("quippy.Potential_Cluster")
class Potential_Cluster(f90wrap.runtime.FortranDerivedType):
    """
    Type(name=potential_cluster)
    
    
    Defined at Potential.fpp lines 636-639
    
    """
    def __init__(self, args_str, inner_pot, error=None, handle=None):
        """
        self = Potential_Cluster(args_str, inner_pot[, error])
        
        
        Defined at Potential.fpp lines 3303-3325
        
        Parameters
        ----------
        args_str : str
        inner_pot : Potential
        error : int
        
        Returns
        -------
        this : Potential_Cluster
        
        Potential type which abstracts all QUIP interatomic potentials
        
        Provides interface to all energy/force/virial calculating schemes,
        including actual calculations, as well as abstract hybrid schemes
        such as LOTF, Force Mixing, ONIOM, and the local energy scheme.
        
        Typically a Potential is constructed from an initialisation
        args_str and an XML parameter file, e.g. in Fortran::
        
        type(InOutput) :: xml_file
        type(Potential) :: pot
        ...
        call initialise(xml_file, 'SW.xml', INPUT)
        call initialise(pot, 'IP SW', param_file=xml_file)
        
        Or, equivaently in Python::
        
        pot = Potential('IP SW', param_filename='SW.xml')
        
        creates a Stillinger-Weber potential using the parameters from
        the file 'SW.xml'. The XML parameters can also be given directly
        as a string, via the `param_str` argument.
        
        The main workhorse is the :meth:`calc` routine, which is used
        internally to perform all calculations, e.g. to calculate forces::
        
        type(Atoms) :: at
        real(dp) :: force(3,8)
        ...
        call diamond(at, 5.44, 14)
        call randomise(at%pos, 0.01)
        call calc(pot, at, force=force)
        
        Note that there is now no need to set the 'Atoms%cutoff' attribute to the
        cutoff of this Potential: if it is less than this it will be increased
        automatically and a warning will be printed.
        The neighbour lists are updated automatically with the
        :meth:`~quippy.atoms.Atoms.calc_connect` routine. For efficiency,
        it's a good idea to set at%cutoff_skin greater than zero to decrease
        the frequency at which the connectivity needs to be rebuilt.
        
        A Potential can be used to optimise the geometry of an
        :class:`~quippy.atoms.Atoms` structure, using the :meth:`minim` routine,
        (or, in Python, via  the :class:`Minim` wrapper class).
        
        .. rubric:: args_str options
        
        ========== ===== ===== ================================================================================
        Name       Type  Value Doc                                                                             
        ========== ===== ===== ================================================================================
        run_suffix None        Suffix to apply to hybrid mark properties$                                      
        r_scale    float 1.0   Rescaling factor for cluster positions                                          
        E_scale    float 1.0   Rescaling factor for cluster energies(and hence also forces)                    
        ========== ===== ===== ================================================================================
        
        
        """
        f90wrap.runtime.FortranDerivedType.__init__(self)
        result = quippy._quippy.f90wrap_potential_cluster_initialise(args_str=args_str, inner_pot=inner_pot._handle, \
            error=error)
        self._handle = result[0] if isinstance(result, tuple) else result
    
    def __del__(self):
        """
        Destructor for class Potential_Cluster
        
        
        Defined at Potential.fpp lines 3327-3329
        
        Parameters
        ----------
        this : Potential_Cluster
        
        """
        if self._alloc:
            quippy._quippy.f90wrap_potential_cluster_finalise(this=self._handle)
    
    def print(self, file=None):
        """
        print(self[, file])
        
        
        Defined at Potential.fpp lines 3336-3345
        
        Parameters
        ----------
        this : Potential_Cluster
        file : Inoutput
        
        """
        quippy._quippy.f90wrap_potential_cluster_print(this=self._handle, file=None if file is None else file._handle)
    
    def cutoff(self):
        """
        potential_cluster_cutoff = cutoff(self)
        
        
        Defined at Potential.fpp lines 3331-3334
        
        Parameters
        ----------
        this : Potential_Cluster
        
        Returns
        -------
        potential_cluster_cutoff : float
        
        Return the cutoff of this 'Potential', in Angstrom. This is the
        minimum neighbour connectivity cutoff that should be used: if
        you're doing MD you'll want to use a slightly larger cutoff so
        that new neighbours don't drift in to range between connectivity
        updates
        """
        potential_cluster_cutoff = quippy._quippy.f90wrap_potential_cluster_cutoff(this=self._handle)
        return potential_cluster_cutoff
    
    def calc(self, at, args_str=None, error=None):
        """
        calc(self, at[, args_str, error])
        
        
        Defined at Potential.fpp lines 3347-3380
        
        Parameters
        ----------
        this : Potential_Cluster
        at : Atoms
        args_str : str
        error : int
        
        Apply this Potential to the Atoms object
        'at'. Atoms%calc_connect is automatically called to update the
        connecticvity information -- if efficiency is important to you,
        ensure that at%cutoff_skin is set to a non-zero value to decrease
        the frequence of connectivity updates.
        optional arguments determine what should be calculated and how
        it will be returned. Each physical quantity has a
        corresponding optional argument, which can either be an 'True'
        to store the result inside the Atoms object(i.e. in
        Atoms%params' or in 'Atoms%properties' with the
        default name, a string to specify a different property or
        parameter name, or an array of the the correct shape to
        receive the quantity in question, as set out in the table
        below.
        
        ================  ============= ================ =========================
        Array argument    Quantity      Shape            Default storage location
        ================  ============= ================ =========================
        ``energy``        Energy        ``()``                  ``energy`` param
        ``local_energy``  Local energy  ``(at.n,)``      ``local_energy`` property
        ``force``         Force         ``(3,at.n)``     ``force`` property
        ``virial``        Virial tensor ``(3,3)``        ``virial`` param
        ``local_virial``  Local virial  ``(3,3,at.n)``   ``local_virial`` property
        ================  ============= ================ =========================
        
        The 'args_str' argument is an optional string  containing
        additional arguments which depend on the particular Potential
        being used.
        
        Not all Potentials support all of these quantities: an error
        will be raised if you ask for something that is not supported.
        
        .. rubric:: args_str options
        
        =============== ==== ===================== ============================================================
        Name            Type Value                 Doc                                                         
        =============== ==== ===================== ============================================================
        run_suffix      None trim(this%run_suffix) No help yet. This source file was $LastChangedBy$           
        energy          None                       No help yet. This source file was $LastChangedBy$           
        force           None                       No help yet. This source file was $LastChangedBy$           
        virial          None                       No help yet. This source file was $LastChangedBy$           
        local_energy    None                       No help yet. This source file was $LastChangedBy$           
        local_virial    None                       No help yet. This source file was $LastChangedBy$           
        single_cluster  bool F                     If true, calculate all active/transition atoms with a       
                                                   single big cluster                                          
        little_clusters bool F                     If true, calculate forces(only) by doing each atom          
                                                   separately surrounded by a little buffer cluster            
        =============== ==== ===================== ============================================================
        
        
        """
        quippy._quippy.f90wrap_potential_cluster_calc(this=self._handle, at=at._handle, args_str=args_str, error=error)
    
    @property
    def inner_pot(self):
        """
        Element inner_pot ftype=type(potential) pytype=Potential
        
        
        Defined at Potential.fpp line 637
        
        """
        inner_pot_handle = quippy._quippy.f90wrap_potential_cluster__get__inner_pot(self._handle)
        if tuple(inner_pot_handle) in self._objs:
            inner_pot = self._objs[tuple(inner_pot_handle)]
        else:
            inner_pot = Potential.from_handle(inner_pot_handle)
            self._objs[tuple(inner_pot_handle)] = inner_pot
        return inner_pot
    
    @inner_pot.setter
    def inner_pot(self, inner_pot):
        inner_pot = inner_pot._handle
        quippy._quippy.f90wrap_potential_cluster__set__inner_pot(self._handle, inner_pot)
    
    @property
    def r_scale_pot1(self):
        """
        Element r_scale_pot1 ftype=real(dp) pytype=float
        
        
        Defined at Potential.fpp line 638
        
        """
        return quippy._quippy.f90wrap_potential_cluster__get__r_scale_pot1(self._handle)
    
    @r_scale_pot1.setter
    def r_scale_pot1(self, r_scale_pot1):
        quippy._quippy.f90wrap_potential_cluster__set__r_scale_pot1(self._handle, r_scale_pot1)
    
    @property
    def e_scale_pot1(self):
        """
        Element e_scale_pot1 ftype=real(dp) pytype=float
        
        
        Defined at Potential.fpp line 638
        
        """
        return quippy._quippy.f90wrap_potential_cluster__get__e_scale_pot1(self._handle)
    
    @e_scale_pot1.setter
    def e_scale_pot1(self, e_scale_pot1):
        quippy._quippy.f90wrap_potential_cluster__set__e_scale_pot1(self._handle, e_scale_pot1)
    
    @property
    def run_suffix(self):
        """
        Element run_suffix ftype=character(string_length) pytype=str
        
        
        Defined at Potential.fpp line 639
        
        """
        return quippy._quippy.f90wrap_potential_cluster__get__run_suffix(self._handle)
    
    @run_suffix.setter
    def run_suffix(self, run_suffix):
        quippy._quippy.f90wrap_potential_cluster__set__run_suffix(self._handle, run_suffix)
    
    def __str__(self):
        ret = ['<potential_cluster>{\n']
        ret.append('    inner_pot : ')
        ret.append(repr(self.inner_pot))
        ret.append(',\n    r_scale_pot1 : ')
        ret.append(repr(self.r_scale_pot1))
        ret.append(',\n    e_scale_pot1 : ')
        ret.append(repr(self.e_scale_pot1))
        ret.append(',\n    run_suffix : ')
        ret.append(repr(self.run_suffix))
        ret.append('}')
        return ''.join(ret)
    
    _dt_array_initialisers = []
    

def print_hook(x, dx, e, do_print=None, am_data=None):
    """
    done = print_hook(x, dx, e[, do_print, am_data])
    
    
    Defined at Potential.fpp lines 1510-1575
    
    Parameters
    ----------
    x : float array
    dx : float array
    e : float
    do_print : bool
    am_data : str array
    
    Returns
    -------
    done : bool
    
    """
    done = quippy._quippy.f90wrap_print_hook(x=x, dx=dx, e=e, do_print=do_print, am_data=am_data)
    return done

def energy_func(x, am_data=None):
    """
    energy_func = energy_func(x[, am_data])
    
    
    Defined at Potential.fpp lines 1584-1632
    
    Parameters
    ----------
    x : float array
    am_data : str array
    
    Returns
    -------
    energy_func : float
    
    """
    energy_func = quippy._quippy.f90wrap_energy_func(x=x, am_data=am_data)
    return energy_func

def gradient_func(x, am_data=None):
    """
    gradient_func = gradient_func(x[, am_data])
    
    
    Defined at Potential.fpp lines 1637-1742
    
    Parameters
    ----------
    x : float array
    am_data : str array
    
    Returns
    -------
    gradient_func : float array
    
    """
    gradient_func = quippy._quippy.f90wrap_gradient_func(x=x, am_data=am_data)
    return gradient_func

def max_rij_change(last_connect_x, x, r_cut, lat_factor):
    """
    max_rij_change = max_rij_change(last_connect_x, x, r_cut, lat_factor)
    
    
    Defined at Potential.fpp lines 1948-1971
    
    Parameters
    ----------
    last_connect_x : float array
    x : float array
    r_cut : float
    lat_factor : float
    
    Returns
    -------
    max_rij_change : float
    
    """
    max_rij_change = quippy._quippy.f90wrap_max_rij_change(last_connect_x=last_connect_x, x=x, r_cut=r_cut, \
        lat_factor=lat_factor)
    return max_rij_change

def prep_atoms_deform_grad(deform_grad, at, am):
    """
    prep_atoms_deform_grad(deform_grad, at, am)
    
    
    Defined at Potential.fpp lines 1974-1979
    
    Parameters
    ----------
    deform_grad : float array
    at : Atoms
    am : Potential_Minimise
    
    """
    quippy._quippy.f90wrap_prep_atoms_deform_grad(deform_grad=deform_grad, at=at._handle, am=am._handle)

def fix_atoms_deform_grad(deform_grad, at, am):
    """
    fix_atoms_deform_grad(deform_grad, at, am)
    
    
    Defined at Potential.fpp lines 1982-1989
    
    Parameters
    ----------
    deform_grad : float array
    at : Atoms
    am : Potential_Minimise
    
    """
    quippy._quippy.f90wrap_fix_atoms_deform_grad(deform_grad=deform_grad, at=at._handle, am=am._handle)

def unpack_pos_dg(xx, at_n, at_pos, dg, lat_factor):
    """
    unpack_pos_dg(xx, at_n, at_pos, dg, lat_factor)
    
    
    Defined at Potential.fpp lines 1992-2000
    
    Parameters
    ----------
    xx : float array
    at_n : int
    at_pos : float array
    dg : float array
    lat_factor : float
    
    """
    quippy._quippy.f90wrap_unpack_pos_dg(xx=xx, at_n=at_n, at_pos=at_pos, dg=dg, lat_factor=lat_factor)

def pack_pos_dg(x2d, dg2d, x, lat_factor):
    """
    pack_pos_dg(x2d, dg2d, x, lat_factor)
    
    
    Defined at Potential.fpp lines 2003-2016
    
    Parameters
    ----------
    x2d : float array
    dg2d : float array
    x : float array
    lat_factor : float
    
    """
    quippy._quippy.f90wrap_pack_pos_dg(x2d=x2d, dg2d=dg2d, x=x, lat_factor=lat_factor)

def constrain_virial(self, virial):
    """
    constrain_virial(self, virial)
    
    
    Defined at Potential.fpp lines 3722-3758
    
    Parameters
    ----------
    at : Atoms
    virial : float array
    
    """
    quippy._quippy.f90wrap_constrain_virial(at=self._handle, virial=virial)

def get_array_hack_restraint_i():
    """
    Element hack_restraint_i ftype=integer  pytype=int
    
    
    Defined at Potential.fpp line 235
    
    """
    global hack_restraint_i
    array_ndim, array_type, array_shape, array_handle = \
        quippy._quippy.f90wrap_potential_module__array__hack_restraint_i(f90wrap.runtime.empty_handle)
    if array_handle in _arrays:
        hack_restraint_i = _arrays[array_handle]
    else:
        hack_restraint_i = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                f90wrap.runtime.empty_handle,
                                quippy._quippy.f90wrap_potential_module__array__hack_restraint_i)
        _arrays[array_handle] = hack_restraint_i
    return hack_restraint_i

def set_array_hack_restraint_i(hack_restraint_i):
    globals()['hack_restraint_i'][...] = hack_restraint_i

def get_hack_restraint_r():
    """
    Element hack_restraint_r ftype=real(dp) pytype=float
    
    
    Defined at Potential.fpp line 236
    
    """
    return quippy._quippy.f90wrap_potential_module__get__hack_restraint_r()

def set_hack_restraint_r(hack_restraint_r):
    quippy._quippy.f90wrap_potential_module__set__hack_restraint_r(hack_restraint_r)

def get_hack_restraint_k():
    """
    Element hack_restraint_k ftype=real(dp) pytype=float
    
    
    Defined at Potential.fpp line 236
    
    """
    return quippy._quippy.f90wrap_potential_module__get__hack_restraint_k()

def set_hack_restraint_k(hack_restraint_k):
    quippy._quippy.f90wrap_potential_module__set__hack_restraint_k(hack_restraint_k)


_array_initialisers = [get_array_hack_restraint_i]
_dt_array_initialisers = []

try:
    for func in _array_initialisers:
        func()
except ValueError:
    logging.debug('unallocated array(s) detected on import of module "potential_module".')

for func in _dt_array_initialisers:
    func()

# Generated automatically using the command :
# c++2py ../../c++/triqs_ctint/solver.hpp -p --members_read_only -N triqs_ctint -a triqs_ctint -m triqs_ctint -o triqs_ctint --moduledoc="The triqs_ctint python module" -C triqs --cxxflags="-std=c++17" --target_file_only
from cpp2py.wrap_generator import *

# The module
module = module_(full_name = "triqs_ctint", doc = r"The triqs_ctint python module", app_name = "triqs_ctint")

# Imports
module.add_imports(*['triqs.gf'])

# Add here all includes
module.add_include("triqs_ctint/solver.hpp")

# Add here anything to add in the C++ code at the start, e.g. namespace using
module.add_preamble("""
#include <cpp2py/converters/string.hpp>
#include <triqs/cpp2py_converters/gf.hpp>

using namespace triqs_ctint;
""")

module.add_enum("spin", ['spin::up', 'spin::down'], "triqs_ctint", doc = r"""""")

# The class solver
c = class_(
        py_type = "Solver",  # name of the python class
        c_type = "triqs_ctint::solver",   # name of the C++ class
        doc = r"""""",   # doc of the C++ class
        hdf5 = False,
)

c.add_constructor("""(double beta_, int n_iw = 1024, int n_tau = 100001)""", doc = r"""Construct a ctint solver""")

c.add_method("""void solve (double U, double delta, int n_cycles, int length_cycle = 50, int n_warmup_cycles = 5000, std::string random_name = \"\", int max_time = -1)""",
             doc = r"""Method that performs the QMC calculation""")

c.add_property(name = "G0_iw",
               getter = cfunction("block_gf_view<triqs::gfs::imfreq> G0_iw ()"),
               doc = r"""Access non-interacting Matsubara Green function""")

c.add_property(name = "G0_tau",
               getter = cfunction("block_gf_view<triqs::gfs::imtime> G0_tau ()"),
               doc = r"""Access non-interacting imaginary-time Green function""")

c.add_property(name = "G_iw",
               getter = cfunction("block_gf_view<triqs::gfs::imfreq> G_iw ()"),
               doc = r"""Access interacting Matsubara Green function""")

module.add_class(c)



module.generate_code()
# Use the constructors
import sys
from railroad import *

#sys.stdout = open('EGFR.html', 'w')

print('<h1>Molecule Types:</h1>')

add('EGFR',
    Diagram(
        "EGFR(",
        Choice(0, Comment("    "),
               'ecd',
               ),
        Choice(0, Comment("    "),
               Sequence('Y1',
                        Choice(0, Comment("    "), '~U', '~P'),)
               ),
        Choice(0, Comment("    "),
               Sequence('Y2',
                        Choice(0, Comment("    "), '~U', '~P'),)
               ),
        ")"

    ))

add('EGF',
    Diagram(
        "EFG(",
        Choice(0, Comment("    "),
               'site',
               ),
        ")"
    )
    )

add('Grb2',
    Diagram(
        "Grb2(",
        Choice(0, Comment("    "),
               'sh2',
               ),
        ")"
    ))

add('Shc',
    Diagram(
        "Shc(",
        Choice(0, Comment("    "),
               Sequence('sh3',
                        Choice(0, Comment("    "), '~U', '~P'),)
               ),
        ")"
    ))

#add('\nSpecies:')
print('<h1>Species:</h1>')

add('EGFR',
    Diagram(
        "EGFR(",
        Choice(0, Comment("    "),
               'ecd',
               ),
        Choice(0, Comment("    "),
               Sequence('Y1',
                        Choice(0, Comment("    "), '~U'),)
               ),
        Choice(0, Comment("    "),
               Sequence('Y2',
                        Choice(0, Comment("    "), '~U'),)
               ),
        ")"

    ))

add('EGF',
    Diagram(
        "EFG(",
        Choice(0, Comment("    "),
               'site',
               ),
        ")"
    )
    )

add('Grb2',
    Diagram(
        "Grb2(",
        Choice(0, Comment("    "),
               'sh2',
               ),
        ")"
    ))

add('Shc_P',
    Diagram(
        "Shc(",
        Choice(0, Comment("    "),
               Sequence('sh3',
                        Choice(0, Comment("    "), '~P'),)
               ),
        ")"
    ))

add('Shc_U',
    Diagram(
        "Shc(",
        Choice(0, Comment("    "),
               Sequence('sh3',
                        Choice(0, Comment("    "), '~U'),)
               ),
        ")"
    ))

print('<h1>Observables:</h1>')

add('O0_EGFR_tot',
    Diagram(
        "EGFR(",
        Choice(0, Skip(),
               'ecd',
               ),
        Choice(0, Skip(),
               Sequence('Y1',
                        Choice(0, Skip(), '~U', '~P'),)
               ),
        Choice(0, Skip(),
               Sequence('Y2',
                        Choice(0, Skip(), '~U', '~P'),)
               ),
        ")"
    ))

add('O0_EGF_tot',
    Diagram(
        "EFG(",
        Choice(0, Skip(),
               'site',
               ),
        ")"
    ))

add('O0_Grb2_tot',
    Diagram(
        "Grb2(",
        Choice(0, Skip(),
               'sh2',
               ),
        ")"
    ))

add('O0_Shc_tot',
    Diagram(
        "Shc(",
        Choice(0, Skip(),
               Sequence('sh3',
                        Choice(0, Skip(), '~U', '~P'),)
               ),
        ")"
    )
    )

add('Dimers',
    Diagram(
        "EGFR(",
        Choice(0, Skip(),
               'ecd',
               ),
        Choice(0, Comment("    "),
               Sequence('tmd',
                        Choice(0, Comment("    "), 'bound'),)
               ),
        Choice(0, Skip(),
               Sequence('Y1',
                        Choice(0, Skip(), '~U', '~P'),)
               ),
        Choice(0, Skip(),
               Sequence('Y2',
                        Choice(0, Skip(), '~U', '~P'),)
               ),
        ")"
    ))

add('Dimers_s',
    Diagram(
        "EGFR(",
        Choice(0, Skip(),
               'ecd',
               ),
        Choice(0, Comment("    "),
               Sequence('tmd',
                        Choice(0, Comment("    "), 'bound'),)
               ),
        Choice(0, Skip(),
               Sequence('Y1',
                        Choice(0, Skip(), '~U', '~P'),)
               ),
        Choice(0, Skip(),
               Sequence('Y2',
                        Choice(0, Skip(), '~U', '~P'),)
               ),
        ")"
    ))

add('Y1',
    Diagram(
        "EGFR(",
        Choice(0, Skip(),
               'ecd',
               ),
        Choice(0, Skip(),
               'tmd',
               ),
        Choice(0, Comment("    "),
               Sequence('Y1',
                        Choice(0, Comment("    "), '~P'),)
               ),
        Choice(0, Skip(),
               Sequence('Y2',
                        Choice(0, Skip(), '~U', '~P'),)
               ),
        ")"
    ))

add('Y2',
    Diagram(
        "EGFR(",
        Choice(0, Skip(),
               'ecd',
               ),
        Choice(0, Skip(),
               'tmd',
               ),
        Choice(0, Skip(),
               Sequence('Y1',
                        Choice(0, Skip(), '~U', '~P'),)
               ),
        Choice(0, Comment("    "),
               Sequence('Y2',
                        Choice(0, Comment("    "), '~P'),)
               ),
        ")"
    ))



#sys.stdout.close

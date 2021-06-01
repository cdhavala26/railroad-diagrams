
import sys
from railroad import *
print('<h1>Molecule Types:</h1>')
add('EGFR',
   	Diagram(
       	"EGFR(",
   	    Choice(0, Comment("    "),
   	           'site',
   	           ),
     	 ")"

   	)
    )

add('EGF',
    Diagram(
        "EFG(",
        Choice(0, Comment("    "),
               'site',
               ),
        ")"
    )
    )
add('Gbr2',
    Diagram(
        "EFG(",
        Choice(0, Comment("    "),
               'site',
               ),
        ")"
    )
    )


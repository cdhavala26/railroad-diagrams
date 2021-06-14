
import sys
from railroad import *
 
print('<h1>Molecules</h1>')
add("EGFR",
    Diagram(
		"EGFR(",
        Choice(0, Comment("    "),
                "ecd",
				),
		
        Choice(0, Comment("    "),
                " tmd",
				),
		
        Choice(0, Comment("    "),
               Sequence(" Y1",
                        Choice(0, Comment("    "),  "~U", "~P"),)
			   ),
				   
        Choice(0, Comment("    "),
               Sequence(" Y2",
                        Choice(0, Comment("    "),  "~U", "~P"),)
			   ),
				    
		")"
	))
	
add("EGF",
    Diagram(
		"EGF(",
        Choice(0, Comment("    "),
                "site",
				),
		 
		")"
	))
	
add("Grb2",
    Diagram(
		"Grb2(",
        Choice(0, Comment("    "),
                "sh2",
				),
		 
		")"
	))
	
add("Shc",
    Diagram(
		"Shc(",
        Choice(0, Comment("    "),
                "sh3",
				),
		
        Choice(0, Comment("    "),
               Sequence(" Y",
                        Choice(0, Comment("    "),  "~U", "~P"),)
			   ),
				    
		")"
	))
	 
print('<h1>Species</h1>')
add("EGFR",
    Diagram(
		"EGFR(",
        Choice(0, Comment("    "),
                "ecd",
				),
		
        Choice(0, Comment("    "),
               Sequence("Y1",
                        Choice(0, Comment("    "),  "~U"),)
			   ),
				   
        Choice(0, Comment("    "),
               Sequence(" Y2",
                        Choice(0, Comment("    "),  "~W"),)
			   ),
				    
		")"
	))
	
add("Grb2",
    Diagram(
		"Grb2(",
        Choice(0, Comment("    "),
                "sh2",
				),
		 
		")"
	))
	
add("Shc",
    Diagram(
		"Shc(",
        Choice(0, Comment("    "),
                "sh3",
				),
		
        Choice(0, Comment("    "),
               Sequence(" Y",
                        Choice(0, Comment("    "),  "~P"),)
			   ),
				    
		")"
	))
	
add("Shc",
    Diagram(
		"Shc(",
        Choice(0, Comment("    "),
                "sh3",
				),
		
        Choice(0, Comment("    "),
               Sequence(" Y",
                        Choice(0, Comment("    "),  "~P"),)
			   ),
				    
		")"
	))
	 
print('<h1>Observables</h1>')
add("EGFR",
    Diagram(
		"EGFR(",
        Choice(0, Comment("    "),
                "ecd",
				),
		
        Choice(0, Comment("    "),
                " tmd",
				),
		
        Choice(0, Comment("    "),
               Sequence(" Y1",
                        Choice(0, Comment("    "),  "~U", "~P"),)
			   ),
				   
        Choice(0, Comment("    "),
               Sequence(" Y2",
                        Choice(0, Comment("    "),  "~U"),)
			   ),
				    
		")"
	))
	
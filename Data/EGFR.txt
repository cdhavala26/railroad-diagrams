
import sys
from railroad import *

add("EGFR",
    Diagram(
		"EGFR(",
        
        Choice(0, Comment("    "),
                "ecd",
				),
			    
        Choice(0, Comment("    "),
               Sequence(" Y1",
                        Choice(0, Comment("    "), "~U", "~P"),)
			   ),
				
        Choice(0, Comment("    "),
               Sequence(" Y2",
                        Choice(0, Comment("    "), "~U", "~P"),)
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
               Sequence("sh",
                        Choice(0, Comment("    "), "~U", "~P"),)
			   ),
				 
		")"
	))
	
add("EGFR",
    Diagram(
		"EGFR(",
        
        Choice(0, Comment("    "),
                "ecd",
				),
			    
        Choice(0, Comment("    "),
               Sequence("Y1",
                        Choice(0, Comment("    "), "~U"),)
			   ),
				
        Choice(0, Comment("    "),
               Sequence(" Y2",
                        Choice(0, Comment("    "), "~U"),)
			   ),
				 
		")"
	))
	
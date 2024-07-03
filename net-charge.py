# Store the human preproinsulin sequence in a variable called preproinsulin:  
preproInsulin = "malwmrllpllallalwgpdpaaafvnqhlcgshlvealylvcgergffytpktrreaedlqvgqvelgggpgagslqplalegslqkrgiveqcctsicslyqlenycn"  
# Store the remaining sequence elements of human insulin in variables:  
lsInsulin = "malwmrllpllallalwgpdpaaa"  
bInsulin = "fvnqhlcgshlvealylvcgergffytpkt"  
aInsulin = "giveqcctsicslyqlenycn"  
cInsulin = "rreaedlqvgqvelgggpgagslqplalegslqkr"  
insulin = bInsulin + aInsulin
 
#Create a new dictionary with key-value pairs
pKR= {'y': 10.07, 'c': 8.18, 'k': 10.53, 'h': 12.48, 'r': 12.48, 'd': 3.65, 'e': 4.25}
 
 
#count() that will count the number of amino acid contributing to net charge
seqCount = {x: float(insulin.count(x)) for x in ['y','c','k','h','r','d','e']}
#sequence of counts
print(seqCount)
 
 
#Variable pH
pH = 0
#While loop that prints net charge from 0 to 14
while (pH <= 14): 
# Loops pH is less than or equal to 14
    netCharge = (
    +(sum({x: ((seqCount[x]*(10**pKR[x]))/((10**pH)+(10**pKR[x]))) \
    for x in ['k','h','r']}.values()))
    -(sum({x: ((seqCount[x]*(10**pH))/((10**pH)+(10**pKR[x]))) \
    for x in ['y','c','d','e']}.values()))
    )
    
    print('{0:.2f}'.format(pH), netCharge) # prints the netCharge format to two decimal places (.2f)
    pH += 1 # increases pH by 1 from 0-14
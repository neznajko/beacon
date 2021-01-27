#! /usr/bin/env python3
from random import choices
################################################################
class beacon:
  def __init__( self, n):              ########################=
    self.w = choices( range( n), k= n) # wires, with repetitions
    self.s = 0                         # switches, bit patterns
    self.n = n                         # copy
    self.m = [ ( 1 << n) - 1]* n       # measurements, switches
  
  def test( self, j):
    result = self.s &( 1 << self.w[ j])
    if result:
      self.m[ j] &= self.s # cross-section
      print( 'Y')
    else:
      print( 'N')

  def flip( self, j):
    p = 1 << j # bit position
    self.s ^= p
    print( "YN"[ not( self.s & p)])

  def done( self):
    for j in range( self.n):
      print( "{0:0{1}b}".format( self.m[ j], self.n)) # ..

  def kommand( self, args):
    lab = args[ 0]
    if 1 < len( args): 
      j = int( args[ 1])
    else:
      j = 0 # defolt
    if lab == 'T':
      self.test( j)
    elif lab == 'C':
      self.flip( j)
    elif lab == 'D':
      self.done()
    else:
      print( f"{lab}: Unknown command.")

#######################################*########################
if __name__ == '__main__':
  n = int( input( "Number of wires: ").strip())
  bcon = beacon( n)
  print( """Commands:
- 'T <wire>'
- 'C <switch>' 
- 'D'
Hit 'Enter' to quit.""")
  while True:
    args = input( "* ").split()
    if not args: break
    bcon.kommand( args)

################################################################ 
# log: - Ha Eakupa, ryeH cTe8aHu, WhoAmI u TeM nogo6Hu ORIG 3000 

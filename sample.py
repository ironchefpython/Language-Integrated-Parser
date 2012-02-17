# Copyright (c) 2012 ironchefpython (https://github.com/ironchefpython)
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import sys, bisect

#MAX_VAL = sys.maxunicode
MAX_VAL = 15

def match(c):
    lookup = [0]
    dests = [None]
    

class State:
    def __init__(self):
        self.transitions = RangeContition(0, sys.maxunicode, None)
    
    def addTransition(self, cond, dest):
        self.lookup = cond.merge

class TransTable:
    def __init__(self, lookup=None, dests=None):
        self.lookup = lookup or [0]
        self.dests = dests or [[]]
        
    def __add__(t1, t2):
        i1, i2 = 0
        lookup = []
        dests = []
        #lookup = [0]
        #dests = [t1.dests[i1] + t2.dests[i2]]
        #i1 += 1
        #i2 += 1
        if i1 == len(t1):
            pass
        elif i2 == len(t2):
            pass
        elif t1.lookup[i1] > t2.lookup[i2]:
            lookup.append(t2.lookup[i2])
            dests.append(t1.dests[i1-1] + t2.dests[i2])
            i2 += 1
        elif t1.lookup[i1] < t2.lookup[i2]:
            lookup.append(t1.lookup[i1])
            dests.append(t1.dests[i1] + t2.dests[i2-1])
            i1 += 1
        elif t1.lookup[i1] == t2.lookup[i2]:
            lookup.append(t1.lookup[i1])
            dests.append(t1.dests[i1] + t2.dests[i2])
            i1 += 1
            i2 += 1
        else:
            assert(False)

    def test(self, val):
        lo = bisect.bisect_right(self.lookup, val)
        return self.dests[lo-1]

# [0, 7] + [0, 5]
        
        
    #def addConditionOld(self, val, dest):
    #    lo = bisect.bisect_left(self.lookup, val)
    #    if lo == len(self.lookup):
    #        self.lookup.append(val)
    #        self.dests.append(dest)
    #        if lo != MAX_VAL:
    #            self.lookup.append(val+1)
    #            self.dests.append(self.dests[lo-1])
    #    elif self.lookup[lo] == val:
    #        if lo != MAX_VAL and self.lookup[lo+1] != val+1:
    #            self.lookup.insert(lo+1, val+1)
    #            self.dests.insert(lo+1, self.dests[lo])
    #        self.dests[lo] = self.dests[lo] + dest
    #    else:
    #        if self.lookup[lo] != val+1:
    #            self.lookup.insert(lo, val+1)
    #            self.dests.insert(lo, self.dests[lo-1])
    #        self.lookup.insert(lo, val)
    #        self.dests.insert(lo, dest)



            
    



x = TransTable()
x.addCondition(9,['9'])
x.addCondition(0,['0'])
x.addCondition(3,['3'])
x.addCondition(15,['15'])
x.addCondition(6,['6'])
x.addCondition(2,['2'])
print x.lookup, x.dests
for i in xrange(MAX_VAL+1):
    pass
#    print i, x.test(i)
sys.exit(0)

class UnicodeDFA:
    def __init__(self, states, delta, start, accepts):
        pass
    
    

    
class Rule:
    pass

    def match():
        pass
    


aObject = (Parser(dict)
    .matches("{")
    .followedBy(optional(aMembers))
    .followedBy("}")
)

aMembers = (Parser(PairList)
    .matches(aPair)
    .followedBy(
        optional(
            matches(",")
            .followedBy(aMembers)
        )
    )
)

aMembers = (Parser(PairList)
    .matches(aPair)
    .followedBy(
        zeroOrMore(
            matches(",")
            .followedBy(aPair)
        )
    )
)


aPair = (Parser(Pair)
    .matches(aString)
    .followedBy(":")
    .followedBy(aValue)
)

aArray = (Parser(Array)
    .matches("{")
    .followedBy(optional(aElements))
    .followedBy("}")
)

aElements = (Parser(ElementsList)
    .matches(aValue)
    .followedBy(
        optional(
            matches(",")
            .followedBy(aElements)
        )
    )
)

aValue = (Parser(Value)
    .matches(aString)
    .orMatches(aNumber)
    .orMatches(aObject)
    .orMatches(aArray)
    .orMatches(aBoolean)
    .orMatches(aNull)
)

aString = (Rule(String)
    .matches("\"")
    .followedBy(zeroOrMore(aChar))
    .followedBy("\"")
)

aChar = (Rule(String)
    .matches("\"")
    .followedBy(zeroOrMore(aChar))
    .followedBy("\"")
)

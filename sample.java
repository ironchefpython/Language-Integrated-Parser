// Copyright (c) 2012 ironchefpython (https://github.com/ironchefpython)
//
// Permission is hereby granted, free of charge, to any person obtaining a copy
// of this software and associated documentation files (the "Software"), to deal
// in the Software without restriction, including without limitation the rights
// to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
// copies of the Software, and to permit persons to whom the Software is
// furnished to do so, subject to the following conditions:
//
// The above copyright notice and this permission notice shall be included in
// all copies or substantial portions of the Software.
//
// THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
// IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
// FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
// AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
// LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
// OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
// SOFTWARE.


public static class PairArrayMap extends HashMap {
    public PairArrayMap(Pair[] pairs) {
        super();
        for (Pair pair : pairs) {
            this.put(pair.getName(), pair.getValue());
        }
    }
}

aObject = new Parser(PairArrayMap.class, new Class[] { Pair[].class })
    .matches("{")
    .followedBy(
        optional(
            matches(aPair)
            .followedBy(
                zeroOrMore(
                    matches(",")
                    .followedBy(aPair)
                )
            )
        )
    )
    .followedBy("}");


public static class Pair {
    private String name;
    private Object value;
    public Pair(String name, Object value) {
        this.name = name;
        this.value = value;
    }
    public String getName() { return name; }
    public Object getValue() { return value; }
}

aPair = new Parser(Pair.class, new Class[] { Name.class, Value.class })
    .matches(aString)
    .followedBy(":", null)
    .followedBy(aValue);

aString = new Parser(StringBuilder.class, newClass[] { CharSequence[].class }, "append")
    .matches("\"")
    .followedBy(zeroOrMore(aChar))
    .followedBy("\"");

aChar = new Parser(String.class)
    .matches(aRegularChar)
    .orMatches(aEscapedChar)
    .orMatches(aUnicodeChar);
    
aRegularChar = new Parser(String.class, newClass[] { char[].class })
    not(
        matches('"')
        .orMatches('\\')
        .orMatches(aControlChar)
    );

aEscapedChar = new Parser(String.class, newClass[] { char[].class })
    .matches('\\')
    .followedBy(
        matches('"')
        .orMatches('\\')
        .orMatches('/')
        .orMatches('b')
        .orMatches('f')
        .orMatches('n')
        .orMatches('r')
        .orMatches('t')
    );

public static class Pair {
    private String name;
    private Object value;
    public Pair(String name, Object value) {
        this.name = name;
        this.value = value;
    }
    public String getName() { return name; }
    public Object getValue() { return value; }
}

aUnicodeChar = new Parser(UnicodeChar.class, newClass[] { char[].class })
    .matches('\\')
    .followedBy('u')
    .followedBy(aHexDigit)
    .followedBy(aHexDigit)
    .followedBy(aHexDigit)
    .followedBy(aHexDigit);



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



aChar = (Rule(String)
    .matches("\"")
    .followedBy(zeroOrMore(aChar))
    .followedBy("\"")
)

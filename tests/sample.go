nil iota true false

42 0600 0xBadFace 0xDEADBEEF 170141183460469231731687303715884105727
0. 72.40 072.40 2.71828 1.e+0 6.67428e-11 1E6 .25 .12345E+5
0i 011i 0.i 2.71828i 1.e+0i 6.67428e-11i 1E6i .25i .12345E+5i

'a' '\t' '\000' '\007' '\377' '\x07' '\xff' '\u12e4' '\U00101238' '\''
'aa' '\xa' '\0'
`abc` "\n" "\"" "Hello, world!\n" "\u65e5xyz\U00008a9e" "\xff\u00FF" `\n
\n`

var x interface{}
var v *T

type T1 string
type T2 T1
type T3 []T1
type T4 T3

uint8 uint16 uint32 uint64 int8 int16 int32 int64 uint int uintptr
float32 float64 complex64 complex128
byte rune

[32]byte
[2*N] struct { x, y int32 }
[1000]*float64
[3][5]int
[2][2][2]float64  // same as [2]([2]([2]float64))

make([]T, length, capacity)
make([]int, 50, 100)
new([100]int)[0:50]

struct {}
struct {
    x, y int
    u float32
    _ float32
    A *[]int
    F func()
}
struct {
    T1
    *T2
    P.T3
    *P.T4
    x, y int
}
struct { T1; *T2; P.T3; *P.T4; float64; z float64; x, y int }
struct {
    microsec  uint64 "field 1"
    serverIP6 uint64 "field 2"
    process   string "field 3"
}
type TreeNode struct {
    left, right *TreeNode
    value *Comparable
}

(s + ".c") f(3.1415, true) Point{1, 2} m["foo"] s[i:j + 1] obj.color f.p[i].x()

func()
func(x int) int
func(a, _ int, z float32) bool
func(a, b int, z float32) (bool)
func(prefix string, values ...int)
func(a, b int, z float64, opt ...interface{}) (success bool)
func(int, int, float64) (float64, *[]int)
func(n int) func(p *T)

// A simple File interface
interface {
    Read(b Buffer) bool
    Write(b Buffer) bool
    Close()
}

func (p T) Read(b Buffer) bool { return /* ... */ }
func (p T) Write(b Buffer) bool { return /* ... */ }
func (p T) Close() { /* ... */ }

type Locker interface {
    Lock()
    Unlock()
}

type ReadWriter interface {
    Read(b Buffer) bool
    Write(b Buffer) bool
}


map[string]int
map[*T]struct{ x, y float64 }
map[string]interface{}

chan T          // can be used to send and receive values of type T
chan<- float64  // can only be used to send float64s
<-chan int      // can only be used to receive ints

chan<- chan int    // same as chan<- (chan int)
chan<- <-chan int  // same as chan<- (<-chan int)
<-chan <-chan int  // same as <-chan (<-chan int)
chan (<-chan int)

make(chan int, 100)

type (
    T0 []string
    T1 []string
    T2 struct{ a, b int }
    T3 struct{ a, c int }
    T4 func(int, float64) *T0
    T5 func(x int, y float64) *[]string
)

T0 and T0
[]int and []int
struct{ a, b *T5 } and struct{ a, b *T5 }
func(x int, y float64) *[]string and func(int, float64) (result *[]string)

const Pi float64 = 3.14159265358979323846
const zero = 0.0         // untyped floating-point constant
const (
    size int64 = 1024
    eof        = -1  // untyped integer constant
)
const a, b, c = 3, 4, "foo"
const u, v float32 = 0, 3

const (
    Sunday = iota
    Monday
    Tuesday
    Wednesday
    Thursday
    Friday
    Partyday
    numberOfDays  // this constant is not exported
)

const (  // iota is reset to 0
    c0 = iota  // c0 == 0
    c1 = iota  // c1 == 1
    c2 = iota  // c2 == 2
)

const (
    a = 1 << iota  // a == 1 (iota has been reset)
    b = 1 << iota  // b == 2
    c = 1 << iota  // c == 4
)

const (
    u         = iota * 42  // u == 0     (untyped integer constant)
    v float64 = iota * 42  // v == 42.0  (float64 constant)
    w         = iota * 42  // w == 84    (untyped integer constant)
)

const x = iota  // x == 0 (iota has been reset)
const y = iota  // y == 0 (iota has been reset)

const (
    bit0, mask0 = 1 << iota, 1<<iota - 1  // bit0 == 1, mask0 == 0
    bit1, mask1                           // bit1 == 2, mask1 == 1
    _, _                                  // skips iota == 2
    bit3, mask3                           // bit3 == 8, mask3 == 7
)

type IntArray [16]int

type (
    Point struct{ x, y float64 }
    Polar Point
)

type Block interface {
    BlockSize() int
    Encrypt(src, dst []byte)
    Decrypt(src, dst []byte)
}

var i int
var U, V, W float64
var k = 0
var x, y float32 = -1, -2
var (
    i       int
    u, v, s = 2.0, 3.0, "bar"
)
var re, im = complexSqrt(-1)
var _, found = entries[name]  // map lookup; only interested in "found"

var d = math.Sin(0.5)  // d is float64
var i = 42             // i is int
var t, ok = x.(T)      // t is T, ok is bool
var n = nil            // illegal

func min(x int, y int) int {
    if x < y {
        return x
    }
    return y
}

func flushICache(begin, end uintptr)  // implemented externally

buffer := [10]string{}             // len(buffer) == 10
intSet := [6]int{1, 2, 3, 5}       // len(intSet) == 6
days := [...]string{"Sat", "Sun"}  // len(days) == 2

f := t.Mv; f(7)   // like t.Mv(7)
f := pt.Mp; f(7)  // like pt.Mp(7)
f := pt.Mv; f(7)  // like (*pt).Mv(7)
f := t.Mp; f(7)   // like (&t).Mp(7)
f := makeT().Mp   // invalid: result of makeT() is not addressable

var x interface{} = 7  // x has dynamic type int and value 7
i := x.(int)           // i has type int and value 7

type I interface { m() }
var y I
s := y.(string)
r := y.(io.Reader)

switch i := x.(type) {
case nil:
    printString("x is nil")                // type of i is type of x (interface{})
case int:
    printInt(i)                            // type of i is int
case float64:
    printFloat64(i)                        // type of i is float64
case func(int) float64:
    printFunction(i)                       // type of i is func(int) float64
case bool, string:
    printString("type is bool or string")  // type of i is type of x (interface{})
default:
    printString("don't know the type")     // type of i is type of x (interface{})
}

v := x  // x is evaluated exactly once
if v == nil {
    i := v                                 // type of i is type of x (interface{})
    printString("x is nil")
} else if i, isInt := v.(int); isInt {
    printInt(i)                            // type of i is int
} else if i, isFloat64 := v.(float64); isFloat64 {
    printFloat64(i)                        // type of i is float64
} else if i, isFunc := v.(func(int) float64); isFunc {
    printFunction(i)                       // type of i is func(int) float64
} else {
    _, isBool := v.(bool)
    _, isString := v.(string)
    if isBool || isString {
        i := v                         // type of i is type of x (interface{})
        printString("type is bool or string")
    } else {
        i := v                         // type of i is type of x (interface{})
        printString("don't know the type")
    }
}

go Server()
go func(ch chan<- bool) { for { sleep(10); ch <- true; }} (c)

var a []int
var c, c1, c2, c3, c4 chan int
var i1, i2 int
select {
case i1 = <-c1:
    print("received ", i1, " from c1\n")
case c2 <- i2:
    print("sent ", i2, " to c2\n")
case i3, ok := (<-c3):  // same as: i3, ok := <-c3
    if ok {
        print("received ", i3, " from c3\n")
    } else {
        print("c3 is closed\n")
    }
case a[f()] = <-c4:
    // same as:
    // case t := <-c4
    //  a[f()] = t
default:
    print("no communication\n")
}

for {  // send random sequence of bits to c
    select {
    case c <- 0:  // note: no statement, no fallthrough, no folding of cases
    case c <- 1:
    }
}

select {}  // block forever



lock(l)
defer unlock(l)  // unlocking happens before surrounding function returns

// prints 3 2 1 0 before surrounding function returns
for i := 0; i <= 3; i++ {
    defer fmt.Print(i)
}

// f returns 1
func f() (result int) {
    defer func() {
        result++
    }()
    return 0
}

import   "lib/math"         // math.Sin
import m "lib/math"         // m.Sin
import . "lib/math"         // Sin
import _ "lib/math"

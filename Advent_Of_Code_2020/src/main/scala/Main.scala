import scala.util.chaining._

import AOC._
import Day0._
import scala.math.{hypot}

/**
* Welcome to my Advent of Code solutions for 2020!
*
* Goals:
* - Write idiomatic, almost purely functional Scala. 
* - Try and make Scala look like an attractive 'statically typed Python'
    (https://www.handsonscala.com/)
* - Minimize character count per solution. Line count doesn't matter. 
*   Code should be long and thin. Descriptive variable names are still required.
* - Fiddle with Scala 3 features like enums, givens and extensions methods.
* - Don't use external dependencies.
*/
class Day1(part: Int):
  def run(): Int =
    getDayInputLines(1)
      .map(_.toInt)
      .combinations(if part == 1 then 2 else 3)
      .filter(_.sum == 2020)
      .map(_.product)
      .next
      .tap(result => println(s"Day 1-$part: $result"))

///////////////////////////////////////////////////////////////////////////////

class Day2(part: Int):
  def isValid(min: Int, max: Int, char: Char, password: String): Boolean =
    if part == 1 
    then (min to max).contains(password.count(_ == char))
    else
      // Toboggan Corporate Policies have no concept of "index zero"!
      (password(min - 1) == char) ^ (password(max - 1) == char)

  def run(): Int =
    val pattern = "(\\d+)-(\\d+) (\\w): (\\w+)".r
    
    getDayInputLines(2).count {
      case pattern(min, max, char, password) =>
        isValid(min.toInt, max.toInt, char.toCharArray.head, password)
    }
    .tap(result => println(s"Day 2-$part: $result"))

///////////////////////////////////////////////////////////////////////////////

class Day3(part: Int):
  def run(): Long =
    val trees: Array[Array[Char]] = 
      getDayInputLines(3).map(_.toCharArray)

    val slopes = 
      if part == 1 then
        List((3, 1))
      else
        List(
          (1, 1),
          (3, 1),
          (5, 1),
          (7, 1),
          (1, 2),
        )

    slopes
      .map { (right, down) => // get all the hits per slope type
        trees
          .takeNth(down) // if we're moving downhill quickly, skip rows
          .zipWithIndex
          .count {
            (row, index) =>
                // loop around the map when we fall off the edge
                row((index * right) % row.length) == '#' 
          }
          .toLong // we don't want our numbers to loop around either!
      }
      .product
      .tap(result => println(s"Day 3-${part}: ${result}"))

///////////////////////////////////////////////////////////////////////////////

class Day4(part: Int):
  val REQUIRED_KEYS = Set("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid")
  val EYE_COLORS    = Set("amb", "blu", "brn", "gry", "grn", "hzl", "oth")

  def isValid(passport: Map[String, String]): Boolean =
    val requiredKeysPresent = REQUIRED_KEYS.subsetOf(passport.keys.toSet)

    if (part == 1) 
      requiredKeysPresent
    else
      requiredKeysPresent &&
      (1920 to 2002).contains(passport("byr").toInt) &&
      (2010 to 2020).contains(passport("iyr").toInt) &&
      (2020 to 2030).contains(passport("eyr").toInt) &&
      "^#[0-9a-f]{6}$".r.matches(passport("hcl")) &&
      "^[0-9]{9}$".r.matches(passport("pid")) &&
      EYE_COLORS.contains(passport("ecl")) &&
      (passport("hgt") match 
        case s"${n}cm" => (150 to 193).contains(n.toInt)
        case s"${n}in" => (59 to 76).contains(n.toInt) 
        case _         => false)

  def run() =
    getDayInputGroups(4)
      .count { passport =>
        passport
          .split("\\s") // split on whitespace to give kv pairs
          .map { // split on ':' and build kv tuples
            case s"$key:$value" => key -> value
          }
          .toMap // passports are just k:v pairs
          .pipe(isValid) // welcome home
      }
      .tap(result => println(s"Day 4-$part: $result"))

///////////////////////////////////////////////////////////////////////////////

class Day5(part: Int):
  def parse(xs: String): Int =
    xs
      .replace('F', '0')
      .replace('B', '1')
      .replace('L', '0')
      .replace('R', '1')
      .pipe(b => Integer.parseInt(b, 2))

  def run() =
    getDayInputLines(5)
      .map(parse) // don't need binary search, just treat it as a binary number
      .tap(ids => println(s"Day 5-1: ${ids.max}")) // big plane
      .sorted
      .sliding(2) // turn to your neighbour, build tuples
      .find { case Array(a, b) => a + 1 != b } // find the gap
      .get // get the gap
      .pipe(_.head + 1) // slot yourself (politely) into the middle of the gap
      .tap(result => println(s"Day 5-2: $result"))

///////////////////////////////////////////////////////////////////////////////

class Day6(part: Int):
  def run() =
    getDayInputGroups(6)
      .map { group => 
        group
          .split("\n")
          .map(_.toSet)
          .reduce { (a, b) =>
            if part == 1 then
              a.union(b)
            else 
              a.intersect(b)
          }
          .size
      }
      .sum
      .tap(result => println(s"Day 6-${part}: $result"))
      
///////////////////////////////////////////////////////////////////////////////

class Day7(part: Int):
  extension [A](graph: Map[A, Set[A]]):
    def parents(child: A): Set[A] =
      graph.collect {
        case (parent, children) if children.contains(child) => 
          parent
      }.toSet

    def ancestors(child: A): Set[A] =
      val p = parents(child)
      p.union(
        p.flatMap(ancestors(_))
      )

  def run() =
    val bags = "(\\d+) ([\\w\\s]+) bag".r

    val multigraph: Map[String, Map[String, Int]] = 
      getDayInputLines(7)
        .map { 
          case s"$parent bags contain $children" =>
            parent ->
              bags.findAllIn(children).map { 
                case bags(count, name) => 
                  name -> count.toInt
              }.toMap
        }
        .toMap
      
    val graph: Map[String, Set[String]] = 
      multigraph.view.mapValues(_.keys.toSet).toMap

    graph
      .ancestors("shiny gold")
      .size
      .tap(result => println(s"Day 7-1: $result"))

    def bagsInside(key: String): Int =
      val children: Map[String, Int] = multigraph(key)

      children.map { (bag, count) =>
        count + (count * bagsInside(bag))
      }.sum

    bagsInside("shiny gold")
      .tap(result => println(s"Day 7-2: $result"))
      
///////////////////////////////////////////////////////////////////////////////

class Day8(part: Int):
  import scala.collection.mutable.HashSet

  enum Termination:
    case InfiteLoop(acc: Int);
    case Normal(acc: Int);

  def execute(tape: Array[String]): Termination =
    var pc = 0
    var acc = 0
    val seen = HashSet[Int]()

    while true do
      if pc == tape.length then
        return Termination.Normal(acc)
      else if seen.contains(pc) then 
        return Termination.InfiteLoop(acc)
        
      seen += pc

      tape(pc) match
        case s"acc $d" =>
          acc += d.toInt
          pc +=1 
        case s"jmp $d" =>
          pc += d.toInt
        case s"nop $d" => 
          pc += 1
    ???

  def run() =
    val tape = getDayInputLines(8)

    if part == 1 then
      execute(tape) match
        case Termination.InfiteLoop(acc) => println(s"Day 8-1: $acc")
        case _ => 
    else
      tape
        .zipWithIndex
        .collect { 
          case (s"jmp $d", index) =>
            // flip the operation and run the program
            execute(tape.updated(index, s"nop $d"))
          case (s"nop $d", index) => 
            execute(tape.updated(index, s"jmp $d"))
        }
        .collect { case Termination.Normal(acc) => acc } 
        .head
        .tap(result => println(s"Day 8-2: $result"))

///////////////////////////////////////////////////////////////////////////////

class Day9(part: Int):
  def run(): Unit =
    val input = getDayInputLines(9).map(_.toLong)
    val invalid = input
      .sliding(25 + 1) // preamble + the thing we're checking
      .find { window => 
        !window
          .init // init is everything except the last
          .combinations(2)
          .map(_.sum)
          .contains(window.last)
      }
      .get
      .last // of the window
      .tap(result => println(s"Day 9-1: $result"))

    var (from, until) = (0, 1)

    while true do
      val window = input.slice(from, until)

      if window.sum < invalid then
        until += 1
      else if window.sum == invalid then
        println(s"Day 9-2: ${window.min + window.max}")
        return
      else
        from += 1 

///////////////////////////////////////////////////////////////////////////////

class Day10(part: Int):

  def run() =
    val bag = getDayInputLines(10)
      .map(_.toInt)
      .sorted
      // add the charging outlet and device adapter
      .pipe(bag => 0 +: bag :+ bag.last + 3)
    
    bag
      .sliding(2)
      .map { case Array(a, b) => b - a } // find the differences
      .toSeq
      .pipe(differences => differences.count(_ == 1) * differences.count(_ == 3))
      .tap(result => println(s"Day 10-1: $result"))


    // for each adapter, we want to store the cumulative possible paths to it
    val counts = collection.mutable.Map[Int, Long]()
    // the first adapter has an implicit path to it
    counts(bag.head) = 1

    for adapter <- bag.tail do
      // collect the total number paths from the predecessors 
      counts(adapter) = 
        // an adapter that does not exist does not have paths to it
        counts.getOrElse(adapter - 1, 0L) +
        counts.getOrElse(adapter - 2, 0L) +
        counts.getOrElse(adapter - 3, 0L)

    println(s"Day 10-2: ${counts(bag.last)}")

///////////////////////////////////////////////////////////////////////////////

class Day11(part: Int):
  def step(grid: Grid[Char], shape: Complex): Grid[Char] =
    val distance = math.max(grid.shape.re, grid.shape.im)

    grid
      .map { (position, contents) =>
        val adjacent: List[Char] = grid.getQueenLines(
          position, 
          distance=if part == 1 then 1 else distance
        )

        val change = contents match {
          case 'L' if !adjacent.contains('#') => 
            '#' 
          case '#' if adjacent.count(_ == '#') >= (if part == 1 then 4 else 5) => 
            'L' 
          case _ => 
            contents
        }

        position -> change
      }

  def run(): Unit =
    var grid: Grid[Char] = getDayInputGrid(11)

    while true do
      val stepped = step(grid, grid.shape)
      if stepped != grid then
        grid = stepped
      else
        val seatsOccupied = grid.values.count(_ == '#')
        println(s"Day 11-$part: $seatsOccupied")
        return

///////////////////////////////////////////////////////////////////////////////

class Day13(part: Int):
  def run() =
    val inputLines = getDayInputLines(13)
    val timestamp = inputLines(0).toInt
    val busses = inputLines(1).split(',')

    busses
      .flatMap(_.toIntOption) // toss the 'x's
      .map { bus =>
        // remainder is time past last bus :. wait is `bus - rem`
        bus - (timestamp % bus) -> bus
      }
      .min // Scala ords by the first elem
      .tap((mod, bus) => println(s"Day 13-1: ${mod * bus}"))

    val busWithIndex = busses
      .zipWithIndex
      .filter { (bus, index) => bus != "x" }
      .map { (bus, index) => (bus.toInt, index) }

    var t: Long = 0
    var step: Long = busWithIndex.head._1

    for (bus, index) <- busWithIndex.tail do
      // check whether each bus is t aligned (Q P U  A L I G N E D)
      while (t + index) % bus != 0 do
        t += step
      // once the bus is aligned, multiply the step size by the current bus
      // to keep all previous steps aligned
      step *= bus

    println(s"Day 13-2: ${t}")

///////////////////////////////////////////////////////////////////////////////

object Day0:
  extension [A](ss: Traversable[A]):
    def takeNth(n: Int): Traversable[A] = 
      ss.zipWithIndex.collect { case (x, i) if i % n == 0 => x }

  object Complex {
    val N = Complex(im = 1)
    val S = Complex(im = -1)
    val E = Complex(re = 1)
    val W = Complex(re = -1)
    val NE = N + E
    val SE = S + E
    val SW = S + W
    val NW = N + W

    val ROOK = List(N, S, E, W)
    val BISHOP = List(NE, SE, SW, NW)
    val QUEEN = ROOK ++ BISHOP
  }

  case class Complex(re: Int = 0, im: Int = 0):
    import Complex._

    def + (that: Complex) = Complex(re + that.re, im + that.im)
    def - (that: Complex) = Complex(re - that.re, im - that.im)
    def * (that: Complex) = Complex(
      re * that.re - im * that.im, 
      re * that.im + im * that.re
    )

    def turnLeft() = this * Complex(im = 1)
    def turnRight() = this * Complex(im = -1)
    def turnAround() = this * Complex(re = -1)
    def cityblockDistance = re.abs + im.abs

    def queenLines(distance: Int = 1): List[Complex] =
      (for {
        step <- (1 to distance)
        direction <- QUEEN
      } yield (direction * Complex(re=distance)) + this).toList

  type Grid[A] = Map[Complex, A]

  extension [A](grid: Grid[A]):
    def getQueenLines(key: Complex, distance: Int = 1): List[A] =
      key.queenLines().map(grid.get).flatten
    
    def shape: Complex = 
      implicit val unsafeHypotenuseOrdering: Ordering[Complex] = 
        new Ordering[Complex]:
          def compare(a: Complex, b: Complex): Int =
            hypot(a.re, a.im).toInt.compare(hypot(b.re, b.im).toInt)

      grid.keys.max(unsafeHypotenuseOrdering)

  def printGrid(grid: Grid[Char]) =
      val shape = grid.shape
      (0 to shape.im).map { y => 
        (0 to shape.re).map { x =>
          val target = Complex(im=y, re=x)
          grid(target)
        }.mkString
      }.mkString("\n")

///////////////////////////////////////////////////////////////////////////////

object AOC:
  def getDayInput(number: Int): String =
    val source = scala.io.Source.fromFile(s"inputs/day_$number.txt")
    try source.mkString.trim finally source.close()

  def getDayInputLines(number: Int): Array[String] =
    getDayInput(number).split('\n')

  def getDayInputGroups(number: Int): Array[String] =
    getDayInput(number).split("\n\n")

  def getDayInputGrid(number: Int): Grid[Char] =
    val coords = for {
      (i, y) <- getDayInputLines(number).zipWithIndex // tag the rows
      (j, x) <- i.zipWithIndex // tag the colums
    } yield Complex(re=x, im=y) -> j

    coords.toMap

object Main:
  def time[R](block: => R): R = {
    val t0 = System.nanoTime()
    val result = block // evaluate
    val t1 = System.nanoTime()
    println(s"Elapsed time: ${(t1 - t0) / 1000000}ms")
    result
  }

  def main(args: Array[String]): Unit =
    time {
      Day1(part=1).run() // 365619
      Day1(part=2).run() // 236873508
    }

    time {
      Day2(part=1).run() // 620
      Day2(part=2).run() // 727
    }

    time {
      Day3(part=1).run() // 265
      Day3(part=2).run() // 3154761400
    }

    time {
      Day4(part=1).run() // 254
      Day4(part=2).run() // 184
    }

    time { 
      Day5(part=1+2).run() // 994 + 741
    } 

    time {
      Day6(part=1).run() // 6530
      Day6(part=2).run() // 3323
    }

    time {
      Day7(part=1+2).run() // 211 + 12414
    }

    time {
      Day8(part=1).run() // 1753
      Day8(part=2).run() // 733
    }

    time {
      Day9(part=1+2).run() // 25918798 + 3340942
    }

    time {
      Day10(part=1+2).run()
    }

    time {
      Day11(part=1).run()
      Day11(part=2).run()
    }

    time {
      Day13(part=1+2).run()
    }

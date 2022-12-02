import $file.Day0

var history: Seq[(Int, Int, Int)] = List()

implicit class TripleOps(val self: (Int, Int, Int)) extends AnyVal {
  def +(other: (Int, Int, Int)) =
    (self._1 + other._1, self._2 + other._2, self._3 + other._3)

  def stepsFromOrigin: Int = 
    (Math.abs(self._1) + Math.abs(self._2) + Math.abs(self._3)) / 2
}

def parse(xs: String): (Int, Int, Int) = xs match {
  case "nw" => (-1, 1, 0)
  case "n" => (0, 1, -1)
  case "ne" => (1, 0, -1)
  case "sw" => (-1, 0, 1) 
  case "s" => (0, -1, 1) 
  case "se" => (1, -1, 0)
} 

def reducer(acc: (Int, Int, Int), x: (Int, Int, Int)) = {
  history = history :+ (acc + x)
  acc + x
}

println(s"Day 11-1: ${Day0.getDayInput(11).split(',').map(parse).reduce(reducer).stepsFromOrigin}") // 818
println(s"Day 11-2: ${history.max.stepsFromOrigin}") // 1596

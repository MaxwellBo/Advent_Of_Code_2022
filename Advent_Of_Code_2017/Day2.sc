import $file.Day0

val grid = Day0.getDayInput(2).split('\n').map(_.split('\t').map(_.toInt))

def evenlyDivides(row: Array[Int]): Int = 
  (for { x <- row; y <- row; if x % y == 0 && x != y } yield x / y).head

println(s"Day 2-1: ${grid.map(x => x.max - x.min).sum}") // 21845
println(s"Day 2-2: ${grid.map(evenlyDivides).sum}") // 191
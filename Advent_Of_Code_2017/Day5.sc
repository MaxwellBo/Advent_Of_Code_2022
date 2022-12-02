import $file.Day0

def part(n: Int): Int = {
  val instructions = Day0.getDayInput(5).split('\n').map(_.toInt)
  var count = 0
  var pointer = 0

  while (0 <= pointer && pointer < instructions.length) {
    val hold = instructions(pointer)
    instructions(pointer) += (if (n == 1) 1 else if (hold >= 3) -1 else 1)
    pointer += hold
    count += 1
  } 
  count
}

println(s"Day 5-1: ${part(1)}") // 354121
println(s"Day 5-2: ${part(2)}") // 27283023
import $file.Day0

val captcha = Day0.getDayInput(1).map(_.asDigit)

def zipWithOffset(offset: Int) =
  captcha.zip(captcha.drop(offset) ++ captcha.take(offset))
    .filter { case (x, y) => x == y }.map(_._1).sum

println(s"Day 1-1: ${zipWithOffset(1)}") // 1150
println(s"Day 1-2: ${zipWithOffset(captcha.length / 2)}") // 1064
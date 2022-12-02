import scala.io.Source

def getDayInput(number: Int) = {
  val source = scala.io.Source.fromFile(s"inputs/day_${number}.txt")
  try source.mkString.trim finally source.close()
}

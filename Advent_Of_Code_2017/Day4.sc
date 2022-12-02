import $file.Day0

val wordArray = Day0.getDayInput(4).split('\n').map(_.split(' '))

def allDistinct(words: Array[String]) = words.distinct.size == words.size

def allUnique(words: Array[String]) =
  (for { x <- words; y <- words; if x != y } yield !x.permutations.contains(y)).forall(identity)

println(s"Day 4-1: ${wordArray.filter(allDistinct).length}") // 451
println(s"Day 4-2: ${wordArray.filter(x => allDistinct(x) && allUnique(x)).length}") // 223
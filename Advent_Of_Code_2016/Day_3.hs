-- http://adventofcode.com/2016/day/3

module Day_3 where

import Data.List
import Data.List.Split

type Triangle = [Int]

main :: IO ()
main = do 
  fileContents <- readFile "inputs/Day_3_input.txt"
  print ("Part 1", part 1 fileContents) -- 1032
  print ("Part 2", part 2 fileContents) -- 1838

isValid :: Triangle -> Bool
isValid (x:y:z:_) = (x + y > z) && (y + z > x) && (z + x > y)

readTriangles :: String -> [Triangle]
readTriangles = (fmap.fmap) read . fmap (words) . lines

part :: Int -> String -> Int
part 1 = length . filter isValid . readTriangles
part 2 = length . filter isValid . transpose' . readTriangles
  where
    transpose' = concat . fmap (chunksOf 3) . transpose

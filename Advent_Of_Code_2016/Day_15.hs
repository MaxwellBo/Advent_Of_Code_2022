-- http://adventofcode.com/2016/day/15

module Day_15 where

import Data.List.Split
import Data.Bifunctor

type Position = Int
type Positions = Int
type Disc = (Position, Positions)

main :: IO ()
main = do
  fileContents <- readFile "inputs/Day_15_input.txt"
  print ("Part 1", part 1 fileContents) -- 148737
  print ("Part 2", part 2 fileContents) -- 2353212

part :: Int -> String -> Int
part n = length . takeWhile (not.allClear) . iterate wait . parseDiscs
  where 
    parseDiscs = compensate
               . (++ (if n == 2 then [(0, 11)] else [])  )
               . (fmap parseDisc) 
               . lines 

compensate :: [Disc] -> [Disc]
compensate = zipWith (\y (a, b)-> (a + y, b)) [1..]

wait :: [Disc] -> [Disc]
wait = fmap.first $ (+1)

allClear :: [Disc] -> Bool
allClear = all (\(p, ps) -> (p `mod` ps) == 0)

parseDisc :: String -> Disc
parseDisc xs = (read $ tok !! 11, read $ tok !! 3)
  where
    tok = splitOn " " . init $ xs

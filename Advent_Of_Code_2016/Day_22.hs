-- https://adventofcode.com/2016/day/22

{-# LANGUAGE RecordWildCards #-}

module Day_22 where 

import Control.Monad
import Data.List.Split

data Node = Node
  { name :: String
  , x :: Int
  , y :: Int
  , size :: Int
  , used :: Int
  , available :: Int
  , percentage :: Int 
  }

instance Show Node where
  show node
    | used node              == 0   = "_" 
    | x node == 32 && y node == 0   = "G"
    | x node == 0  && y node == 0   = "O"
    | size node              >= 150 = "#"
    | otherwise                     = "."

{-
....................#........G
....................#........X
....................#.........
....................#.........
....................#.........
....................#.........
................._..#.........
....................#.........
....................#.........
....................#.........
....................#.........
....................#.........
....................#.........
....................#.........
....................#.........
....................#.........
....................#.........
....................#.........
....................#.........
....................#.........
....................#.........
....................#.........
..............................
..............................
..............................
..............................
..............................
..............................
..............................
..............................
..............................
.............................Y
.............................O
-}

{-- 
To get the _ to position X, it takes 49 shifts. 

To move the G down one node towards the O, it takes 5 shifts in total, 
1 to swap G forward, and 4 to return the _ to infront of the G.

To get G to position Y, there are ((31 * 5) == 155) shifts.

It takes 1 further shift to swap G onto O.

Therefore, the total number of shifts is (49 + (31 * 5) + 1) == 205.
-}

main :: IO ()
main = do
  fileContents <- readFile "inputs/Day_22_input.txt"
  print ("Part 1", partOne fileContents) -- 967
  print "Part 2"
  putStrLn . partTwo $ fileContents -- see map above

partOne :: String -> Int
partOne = length . viablePairs . parseNodes

partTwo :: String -> String
partTwo = showNodes . parseNodes

parseNodes :: String -> [Node]
parseNodes = (fmap parseNode) . drop 2 . lines

showNodes :: [Node] -> String 
showNodes = unlines . (chunksOf 30) . reverse . concat . (fmap show)

viablePairs :: [Node] -> [(Node, Node)]
viablePairs xs = do
  a <- xs
  b <- xs
  guard (used a /= 0)
  guard (name a /= name b)
  guard (used a <= available b)
  return (a, b)

parseNode :: String -> Node
parseNode xs = Node {..}
  where
    name = (flip (!!) 0) . words $ xs
    x = read . tail . (flip (!!) 1) . wordsBy (=='-') $ name
    y = read . tail . (flip (!!) 2) . wordsBy (=='-') $ name
    info = fmap (read . init ) . words $ xs
    size = info !! 1
    used = info !! 2
    available = info !! 3
    percentage = info !! 4

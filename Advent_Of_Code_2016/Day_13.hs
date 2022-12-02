-- http://adventofcode.com/2016/day/13

module Day_13 where

import Data.Bits
import Data.List

type Position = (Int, Int)

seed :: Int
seed = 1350

main :: IO ()
main = do
  print ("Part 1", part 1) -- 92
  print ("Part 2", part 2) -- 124

part :: Int ->  Int
part 1 = length . takeWhile (\x -> not $ ((31, 39) `elem` x)) $ frontier 
part 2 = length . nub . concat . (take 51) $ frontier

frontier :: [[Position]]
frontier = iterate (nub . (move =<<)) [(1,1)]

move :: Position -> [Position]
move (x, y) = filter (isOpen) $ [(x, y + 1), (x, y - 1), (x + 1, y), (x - 1, y)]

isOpen :: Position -> Bool
isOpen (x,y)
  | x < 0 || y < 0 = False
  | otherwise = even . popCount $ (x*x + 3*x + 2*x*y + y + y*y) + seed
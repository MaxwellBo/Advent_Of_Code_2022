-- https://adventofcode.com/2016/day/18

module Day_18 where

import Data.List.Split
import Data.List

main :: IO ()
main = do
  print ("Part 1", part 1) -- 1956
  print ("Part 2", part 2) -- 19995121

seed :: String
seed = ".^^^^^.^^^..^^^^^...^.^..^^^.^^....^.^...^^^...^^^^..^...^...^^.^.^...."
      ++ "...^..^^...^.^.^^..^^^^^...^."

part :: Int -> Int
part n = length . filter (== '.') . concat $ makeRoom (if (n == 1) then 40 
                                                                   else 400000)

makeRoom :: Int -> [String]
makeRoom lines = (take lines) $ (unfoldr deriveNextRow seed)

chunks :: String -> [String]
chunks string = divvy 3 1 ("." ++ string ++ ".")

deriveTrap :: String -> Char
deriveTrap "^^." = '^'
deriveTrap ".^^" = '^'
deriveTrap "^.." = '^'
deriveTrap "..^" = '^'
deriveTrap _     = '.'

deriveNextRow :: String -> Maybe (String, String)
deriveNextRow this = Just (this, next) 
  where
    next = (fmap deriveTrap) . chunks $ this


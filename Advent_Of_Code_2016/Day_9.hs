-- http://adventofcode.com/2016/day/9

module Day_9 where

import Data.List.Split

main :: IO ()
main = do 
  fileContents <- readFile "inputs/Day_9_input.txt"
  print ("Part 1", part 1 fileContents) -- 115118
  print ("Part 2", part 2 fileContents) -- 11107527530

part :: Int -> String -> Int
part n = parseInstructions
  where
    parseInstructions :: String -> Int
    parseInstructions [] = 0
    parseInstructions ('(': xs) = (repeats * children) + parseInstructions rest
      where
        marker =    fst . (break (==')')) $ xs
        (')':xs') = snd . (break (==')')) $ xs
        tok = splitOn "x" marker
        chars = read (tok !! 0)
        repeats = read (tok !! 1)
        (take, rest) = splitAt chars xs'
        children = if n == 1 then length take else (parseInstructions take)
    parseInstructions xss@(x:_) = length lit + parseInstructions xs
      where
        (lit, xs) = break (=='(') $ xss
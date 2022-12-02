-- http://adventofcode.com/2016/day/7

module Day_7 where

import Data.Function ((&))

import Data.List
import Data.List.Split

main :: IO ()
main = do
  fileContents <- readFile "inputs/Day_7_input.txt"
  print ("Part 1", part 1 fileContents) -- 110

part :: Int -> String -> Int
part 1 = length . filter (== True) . (fmap supportsTLS) . lines

tokenize :: String -> ([String], [String])
tokenize xs = (fst part, tail <$> snd part)
  where 
    tok = split (startsWith "[") xs 
        >>= split (dropDelims $ endsWith "]") 
    part = (partition (\x -> head x /= '[')) $ tok

nonEmptySubstrings :: [a] -> [[a]]
nonEmptySubstrings = concatMap (tail . inits) . tails

candidatePalindromes :: String -> [String]
candidatePalindromes = (filter ((4 ==) . length)) . nonEmptySubstrings

isPalindrome :: String -> Bool
isPalindrome xs = ((reverse xs) == xs) 
                    && ((xs !! 0) /= xs !! 1) 

containsPalindrome :: String -> Bool
containsPalindrome = (True `elem`) . (fmap isPalindrome) . candidatePalindromes

supportsTLS :: String -> Bool
supportsTLS xs = outside && not inside
  where 
    tok = tokenize xs
    outside = (any containsPalindrome) $ (fst tok)
    inside = (any containsPalindrome) $ (snd tok)
     
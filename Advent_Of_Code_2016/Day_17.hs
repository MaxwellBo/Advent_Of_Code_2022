-- http://adventofcode.com/2016/day/17

{-# LANGUAGE OverloadedStrings #-}

module Day_17 where

import Data.List
import Data.Ord
import Data.Digest.Pure.MD5 (md5)
import qualified Data.ByteString.Lazy.Char8 as C
import Data.Monoid

type Path = C.ByteString

type Position = ((Int, Int), Path)

seed :: Path
seed = "qljzarfv"

main :: IO ()
main = do
  print ("Part 1", partOne) -- DRLRDDURDR
  print ("Part 2", partTwo) -- 500

partOne :: Path
partOne = C.drop (C.length seed) . head $ paths

partTwo :: Int
partTwo = length . C.unpack . C.drop (C.length seed) . last $ paths

paths :: [Path]
paths = sortBy (comparing C.length)
      . fmap snd
      . filter (isDoor)
      . until (all isDoor) (neighbors =<<)
      $ [((0, 0), seed)]
  where
    isDoor = (==) (3, 3) . fst

neighbors :: Position -> [Position]
neighbors pos@((3, 3), p) = [pos]
neighbors ((x, y), p) = filterAccessible p $  [ ((x, y - 1), p <> "U")
                                              , ((x, y + 1), p <> "D")
                                              , ((x - 1, y), p <> "L")
                                              , ((x + 1, y), p <> "R")
                                              ]

filterAccessible :: Path -> [Position] -> [Position]
filterAccessible p xs = (filter isInBounds) 
                      . (fmap snd) 
                      . (filter isOpen) 
                      $ (zipWith (,) (hash p) xs) 
  where
    hash = show . md5
    isOpen (door, _) = door `elem` ['b'..'f']
    isInBounds ((x, y), _)
      | x < 0 || y < 0 || x > 3 || y > 3 = False
      | otherwise = True
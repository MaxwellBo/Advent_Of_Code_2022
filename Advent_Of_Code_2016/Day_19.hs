-- http://adventofcode.com/2016/day/19

module Day_19 where

import Data.Sequence as S

type Elfs = S.Seq Int

main :: IO ()
main = do
  print ("Part 1", part 1) -- 1830117
  print ("Part 2", part 2) -- 1417887

part :: Int -> Elfs
part n = until ((1==) . S.length) (rotate . (if n == 1 then popNext
                                                       else popOpposite)) $ elfs

elfs :: Elfs
elfs = S.fromList [1..3012210]

popOpposite :: Elfs -> Elfs
popOpposite xs = S.deleteAt index xs
  where
    index = S.length xs `div` 2

popNext :: Elfs -> Elfs
popNext = S.deleteAt 1

rotate :: Elfs -> Elfs
rotate xs = S.drop 1 xs >< S.take 1 xs
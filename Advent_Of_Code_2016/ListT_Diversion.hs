-- http://adventofcode.com/2016/day/13

import Numeric
import Data.Char
import Control.Monad.Writer.Lazy
import Control.Monad.Trans.List

type Position = (Int, Int)

type Stack = ListT (Writer (Sum Int)) Position

seed :: Int
-- seed = 1350
seed = 10

main :: IO ()
main = do 
  print partOne

partOne :: Stack
partOne = until (\x -> (7, 4) `elem` positions x) (>>= move) init
  where
    init = return (1, 1)
    positions = fst . runWriter . runListT
    moves = getSum . execWriter . runListT

move :: Position -> Stack
move (x, y) = do
  lift . tell $ (Sum 1)
  ListT . return . filter (isOpen) $ [(x, y + 1), (x, y - 1), (x + 1, y), (x - 1, y)]

isOpen :: Position -> Bool
isOpen (x,y)
  | x < 0 || y < 0 = False
  | otherwise = even . length . filter (=='1') . binary $ go
  where
    go = (x*x + 3*x + 2*x*y + y + y*y) + seed
    binary x = showIntAtBase 2 intToDigit x ""


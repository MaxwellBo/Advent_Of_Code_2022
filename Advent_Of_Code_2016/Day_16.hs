-- http://adventofcode.com/2016/day/16

module Day_16 where

main :: IO ()
main = do 
  print ("Part 1", part 1) -- 10100011010101011
  print ("Part 2", part 2) -- 01010001101011001
      
seed :: String
seed = "11100010111110100"

part :: Int -> String
part n = checksum $ fillDisk (if n == 1 then 272 
                                        else 35651584) seed

process :: String -> String
process a = a ++ "0" ++ b 
  where
    b = (fmap (\x -> if x == '1' then '0' else '1')) . reverse $ a 

checksum :: String -> String
checksum = (until (odd . length) pairsum) . pairsum

pairsum :: String -> String
pairsum (x:y:xs) 
  | x == y    = '1' : pairsum xs
  | otherwise = '0' : pairsum xs
pairsum _ = []

fillDisk :: Int -> String -> String
fillDisk diskLength = (take diskLength) 
                    . (until (\x -> length x >= diskLength) process)

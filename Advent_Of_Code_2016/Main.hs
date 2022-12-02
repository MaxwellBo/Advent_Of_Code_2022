import qualified Day_3
import qualified Day_4
import qualified Day_7
import qualified Day_9
import qualified Day_13
import qualified Day_15
import qualified Day_16
import qualified Day_17
import qualified Day_18
import qualified Day_19
import qualified Day_22

import System.Process

n :: IO ()
n = putStrLn ""

main :: IO ()
main = do
    putStrLn "Day 1" >> system "python3 Day_1.py" >> n
    putStrLn "Day 2" >> system "python3 Day_2.py" >> n
    putStrLn "Day 3" >> Day_3.main >> n
    putStrLn "Day 4" >> Day_4.main >> n
    putStrLn "Day 5" >> system "python3 Day_5.py" >> n
    putStrLn "Day 6" >> system "python3 Day_6.py" >> n
    putStrLn "Day 7" >> Day_7.main >> n
    putStrLn "Day 8" >> system "julia Day_8.jl" >> n
    putStrLn "Day 9" >> Day_9.main >> n
    putStrLn "Day 10" >> system "python3 Day_10.py" >> n
    system "python3 Day_12_23_25.py" >> n
    putStrLn "Day 13" >> Day_13.main >> n
    putStrLn "Day 14" >> system "python3 Day_14.py" >> n
    putStrLn "Day 15" >> Day_15.main >> n
    putStrLn "Day 16" >> Day_16.main >> n
    putStrLn "Day 17" >> Day_17.main >> n
    putStrLn "Day 18" >> Day_18.main >> n
    putStrLn "Day 19" >> Day_19.main >> n
    putStrLn "Day 20" >> system "python3 Day_20.py" >> n
    putStrLn "Day 21" >> system "python3 Day_21.py" >> n
    putStrLn "Day 22" >> Day_22.main >> n
    putStrLn "Day 24" >> system "python3 Day_24.py" >> n

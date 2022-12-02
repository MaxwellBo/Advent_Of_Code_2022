use std::collections::HashSet;

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn go() {
        let answer = parts(include_str!("inputs/day_1.txt"));
        assert_eq!(answer.0, 576);
        assert_eq!(answer.1, 77674);
    }
}

pub fn parts(input: &str) -> (i32, i32) {
    let vec: Vec<i32> = input
        .lines()
        .map(|x| x.parse::<i32>().unwrap())
        .collect();
    
    let part_1 = vec.iter().sum();

    let mut frequency = 0;
    let mut cache = HashSet::new();
    cache.insert(0);

    for delta in vec.iter().cycle() {
        frequency += delta;

        if !cache.insert(frequency) {
            return (part_1, frequency)
        }
    }
    unreachable!()
}
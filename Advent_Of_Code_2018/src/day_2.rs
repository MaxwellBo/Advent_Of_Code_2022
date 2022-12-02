#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn go() {
        let answer = parts(include_str!("inputs/day_2.txt"));
        assert_eq!(answer.0, 8715);
        assert_eq!(answer.1, "fvstwblgqkhpuixdrnevmaycd");
    }
}

fn has_duplicates(xs: &str, n: usize) -> bool {
    xs.chars().any(|x| xs.matches(x).count() == n)
}

pub fn parts(input: &str) -> (usize, String) {
    let twos    = input.lines().filter(|x| has_duplicates(x, 2)).count();
    let threes  = input.lines().filter(|x| has_duplicates(x, 3)).count();
    let part_1  = twos * threes;

    let v: Vec<_> = input.lines().collect();

    for (i, x) in v[..v.len() - 1].iter().enumerate() {
        for y in v[i + 1..].iter() {

            let diff = x.chars().zip(y.chars()).filter(|(f, s)| f != s).count();

            if diff == 1 {
                let part_2 = x.chars().zip(y.chars())
                    .filter(|(f, s)| f == s)
                    .map(|(f, _)| f)
                    .collect::<String>();

                return (part_1, part_2)
            }
        }
    }
    unreachable!()
}
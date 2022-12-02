use std::collections::HashSet;
use regex::Regex;

#[derive(Debug)]
struct Body {
    x: i32,
    y: i32,
    vx: i32,
    vy: i32
}

impl Body {
    fn step(mut &self) {
        self.x += self.vx;
        self.y += self.vy;
    }
}

let re = Regex::new(r"position=<(.*), (.*)> velocity=<(.*), (.*)>").unwrap();

impl FromStr for Body {
    type Err = ParseIntError;

    fn from_str(s: &str) -> Result<Self, Self::Err> {
        let matches = re.captures_iter(s);

        let x = matches[0].parse::<i32>()?;
        let y = matches[1].parse::<i32>()?;
        let vx = matches[2].parse::<i32>()?;
        let vy = matches[3].parse::<i32>()?;

        Ok(Body { x: x, y: y, vx: vx, vy: vy })
    }
}

pub fn parts(input: &str) -> (i32, i32) {
    let bodies: Vec<Body> = input
        .lines()
        .map(|x| x.parse::<Body>().unwrap())
        .collect();


    for i in 0..100 {
        bodies.step();
    }
}
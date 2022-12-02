mod utils;
mod day_1;
mod day_2;

fn main() {
    let day_1 = day_1::parts(include_str!("inputs/day_1.txt"));
    println!("1-1 {}", day_1.0);
    println!("1-2 {}", day_1.1);

    let day_2 = day_2::parts(include_str!("inputs/day_2.txt"));
    println!("2-1 {}", day_2.0);
    println!("2-2 {}", day_2.1);
}

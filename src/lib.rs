///! Quickly download NASA/NAIF Spice kernels
pub mod py;
pub mod util;

use snafu::prelude::*;

pub type Result<T, E = Error> = std::result::Result<T, E>;

#[derive(Debug, Snafu)]
pub enum Error {}

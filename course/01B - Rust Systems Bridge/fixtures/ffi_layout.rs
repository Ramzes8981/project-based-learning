#![allow(dead_code)]

use std::ffi::c_int;

#[repr(C)]
pub struct Pair {
    pub left: c_int,
    pub right: c_int,
}

pub type CCallback = extern "C" fn(c_int) -> c_int;

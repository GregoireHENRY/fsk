use pyo3::prelude::*;

#[pymodule]
fn fsk(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_class::<MyPythonRustClass>()?;
    m.add_function(wrap_pyfunction!(sum_as_string, m)?)?;
    Ok(())
}

#[pyclass]
pub struct MyPythonRustClass {}

#[pymethods]
impl MyPythonRustClass {}

#[pyfunction]
fn sum_as_string(a: usize, b: usize) -> PyResult<String> {
    Ok((a + b).to_string())
}

use pyo3::prelude::*;

#[pymodule]
#[pyo3(name = "_rs")]
fn python_module(py: Python, m: &Bound<'_, PyModule>) -> PyResult<()> {
    let util = PyModule::new(m.py(), "util")?;

    util.add("DPR", crate::util::DPR)?;
    util.add("RPD", crate::util::RPD)?;

    m.add_submodule(&util)?;
    py.import("sys")?
        .getattr("modules")?
        .set_item("fsk._rs.util", util)?;

    Ok(())
}

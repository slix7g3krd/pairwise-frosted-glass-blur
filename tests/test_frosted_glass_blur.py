import pytest
import render.frosted_glass_blur as mod

CASES = [
    ("distance_radius", (2.0, 10.0)),
    ("own_depth", (1, 2)),
    ("full_res_composite", (1, 2)),
    ("single_blur_pass", (1, 2)),
    ("ui_isolate", (1, 2)),
    ("unified_refract", (1, 2)),
    ("history_weight", (0.5, 0.8)),
    ("roughness_drive", (0.3, 0.7)),
    ("edge_thickness", (0.1, 0.2)),
    ("view_adapt", (0.5, 0.8)),
    ("blur_kernel", (5, 1.2)),
    ("depth_test", (1.0, 2.0)),
    ("sample_offset", (2, 4)),
    ("downsample_guard", (1, 2)),
    ("blend_order", (1, 2)),
]

@pytest.mark.parametrize("fn_name,args", CASES)
def test_contract(fn_name, args):
    fn = getattr(mod, fn_name)
    assert fn(*args) is not None

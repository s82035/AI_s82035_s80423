from typing import Optional
from omni.isaac.core.articulations import ArticulationView
from omni.isaac.core.prims import RigidPrimView


class QuadcopterView(ArticulationView):
    def __init__(
        self,
        prim_paths_expr: str,
        name: Optional[str] = "QuadcopterView"
    ) -> None:
        """[summary]
        """

        super().__init__(
            prim_paths_expr=prim_paths_expr,
            name=name,
            reset_xform_properties=False
        )

        self.rotors = RigidPrimView(prim_paths_expr=f"/World/envs/.*/Quadcopter/rotor[0-3]", reset_xform_properties=False)
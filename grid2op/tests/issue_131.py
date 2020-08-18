#!/usr/bin/env python3

import grid2op
import unittest
import numpy as np


class Issue131Tester(unittest.TestCase):

    def test_issue_131(self):
        env = grid2op.make("rte_case14_realistic")

        # Get forecast after a simulate works
        obs = env.reset()
        obs.simulate(env.action_space({}))
        prod_p_fa, prod_v_fa, load_p_fa, load_q_fa = obs.get_forecasted_inj()
        shapes_a = (prod_p_fa.shape, prod_v_fa.shape,
                    load_p_fa.shape, load_q_fa.shape)

        # Get forecast before any simulate doesnt work
        env.set_id(1)
        obs = env.reset()
        prod_p_fb, prod_v_fb, load_p_fb, load_q_fb = obs.get_forecasted_inj()
        shapes_b = (prod_p_fb.shape, prod_v_fb.shape,
                    load_p_fb.shape, load_q_fb.shape)

        assert shapes_a == shapes_b
        assert np.all(prod_p_fa == prod_p_fb)
        assert np.all(prod_v_fa == prod_v_fb)
        assert np.all(load_p_fa == load_p_fb)
        assert np.all(load_q_fa == load_q_fb)


if __name__ == "__main__":
    unittest.main()

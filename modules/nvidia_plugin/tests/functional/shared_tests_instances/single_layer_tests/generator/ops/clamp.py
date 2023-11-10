#!/usr/bin/env python3

from test_definition_base import CommonTestTraits
from test_definition_base import TestParamsProviderBase
import utils


class TestTraits (CommonTestTraits):
    @property
    def operator_ir_type_string(self):
        return 'Clamp'

    @property
    def test_params_provider_class(self):
        return TestParamsProvider

    @property
    def cpp_test_filename(self):
        return 'activation_slt.cpp'

    @property
    def cpp_test_file_begin_tag(self):
        return '{AUTOGENERATED_TESTS_BEGIN_TAG_CLAMP}'

    @property
    def cpp_test_file_end_tag(self):
        return '{AUTOGENERATED_TESTS_END_TAG_CLAMP}'

    @property
    def template_filename(self):
        return 'clamp.cpp.jinja2'

    @property
    def default_cpp_test_class_name(self):
        return 'ActivationLayerTest'

    @property
    def cpp_alias_name(self):
        return 'AutogenClampParams'


class TestParamsProvider (TestParamsProviderBase):
    def __init__(self, list_of_equal_operators, test_traits):
        super().__init__(list_of_equal_operators, test_traits)

    @property
    def cpp_params_name(self):
        return self.cpp_test_name + '_params'

    @property
    def cpp_params_decl(self):
        return 'const {type} {name} = \n\t{{{{Clamp, {{{min}, {max}}}}}, {{{shape}, {{}}}}}};'.format(
            type = self.test_traits.cpp_alias_name,
            name = self.cpp_params_name,
            min = self.op.data['min'].as_float(),
            max = self.op.data['max'].as_float(),
            shape = utils.cpp_list_from_tuple_of_ints(self.op.input_ports[0].shape))

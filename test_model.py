#!/usr/bin/env python3

from parse_model import parse_model_ios, parse_model_nxos, parse_model_iosxr

def test_parse_model_ios():
    """
    Defines unit tests for Cisco IOS 
    """

    # Create and display some test data
    model_output_list = [
        """
        C2960S Software (C2960S-UNIVERSALK9-M), Version 12.2(55)SE5, RELEASE SOFTWARE (fc1)
        """,
        """
        C2960S Software (C2960S-UNIVERSALK9-M), Version 12, RELEASE SOFTWARE (fc1)
        """,
    ]
    model_answer_list = ["12.2(55)SE5", None]
    for model_output, model_answer in zip(model_output_list, model_answer_list):
        print(model_output)

        # Perform parsing, print structure data and validate
        model_data = parse_model_ios(model_output)
        print(model_data)
        assert model_data == model_answer

def test_parse_model_nxos():
    """
    Defines unit tests for Cisco NX-OS
    """

    # Create and display some test data
    model_output_list = [
        """
        NXOS image file is: bootflash:///nxos.9.2.1.bin
        """,
        """
        NXOS image file is: bootflash:///nxos.9.0.bin
        """,
    ]
    model_answer_list = ["9.2.1", None]
    for model_output, model_answer in zip(model_output_list, model_answer_list):
        print(model_output)

        # Perform parsing, print structure data and validate
        model_data = parse_model_nxos(model_output)
        print(model_data)
        assert model_data == model_answer

def test_parse_model_iosxr():
    """
    Defines unit tests for Cisco IOS-XR 
    """

    # Create and display some test data
    model_output_list = [
        """
        Cisco IOS XR Software, Version 7.0.2
        """,
        """
        Cisco IOS XR Software, Version 7.0.2
        """,
    ]
    model_answer_list = ["7.0.2", None]
    for model_output, model_answer in zip(model_output_list, model_answer_list):
        print(model_output)

        # Perform parsing, print structure data and validate
        model_data = parse_model_ios(model_output)
        print(model_data)
        assert model_data == model_answer
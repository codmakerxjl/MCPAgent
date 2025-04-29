# NOTE: This file has been automatically generated, do not modify!
# Architecture based on https://github.com/mrexodia/ida-pro-mcp (MIT License)
from typing import Annotated, Optional, TypedDict, Generic, TypeVar
from pydantic import Field

T = TypeVar("T")

class Metadata(TypedDict):
    path: str
    module: str
    base: str
    size: str
    md5: str
    sha256: str
    crc32: str
    filesize: str

class Function(TypedDict):
    address: str
    name: str
    size: str

class ConvertedNumber(TypedDict):
    decimal: str
    hexadecimal: str
    bytes: str
    ascii: Optional[str]
    binary: str

class Page(TypedDict, Generic[T]):
    data: list[T]
    next_offset: Optional[int]

class Global(TypedDict):
    address: str
    name: str

class String(TypedDict):
    address: str
    length: int
    string: str

class Xref(TypedDict):
    address: str
    type: str
    function: Optional[Function]

@mcp.tool()
def get_metadata() -> Metadata:
    """Get metadata about the current IDB"""
    return make_jsonrpc_request('get_metadata')

@mcp.tool()
def get_function_by_name(name: Annotated[str, Field(description='Name of the function to get')]) -> Function:
    """Get a function by its name"""
    return make_jsonrpc_request('get_function_by_name', name)

@mcp.tool()
def get_function_by_address(address: Annotated[str, Field(description='Address of the function to get')]) -> Function:
    """Get a function by its address"""
    return make_jsonrpc_request('get_function_by_address', address)

@mcp.tool()
def get_current_address() -> str:
    """Get the address currently selected by the user"""
    return make_jsonrpc_request('get_current_address')

@mcp.tool()
def get_current_function() -> Optional[Function]:
    """Get the function currently selected by the user"""
    return make_jsonrpc_request('get_current_function')

@mcp.tool()
def convert_number(text: Annotated[str, Field(description='Textual representation of the number to convert')], size: Annotated[Optional[int], Field(description='Size of the variable in bytes')]) -> ConvertedNumber:
    """Convert a number (decimal, hexadecimal) to different representations"""
    return make_jsonrpc_request('convert_number', text, size)

@mcp.tool()
def list_functions(offset: Annotated[int, Field(description='Offset to start listing from (start at 0)')], count: Annotated[int, Field(description='Number of functions to list (100 is a good default, 0 means remainder)')]) -> Page[Function]:
    """List all functions in the database (paginated)"""
    return make_jsonrpc_request('list_functions', offset, count)

@mcp.tool()
def list_modules(offset: Annotated[int, Field(description='Offset to start listing from (start at 0)')], count: Annotated[int, Field(description='Number of modules to list (100 is a good default, 0 means remainder)')]) -> Page[dict]:
    """List all modules in the database (paginated)"""
    return make_jsonrpc_request('list_modules', offset, count)

@mcp.tool()
def get_first_module() -> dict:
    """Get the first module in the database"""
    return make_jsonrpc_request('get_first_module')

@mcp.tool()
def get_module_info_by_address(address: Annotated[str, Field(description='Address to get the module info for')]) -> dict:
    """Get the module info for a given address"""
    return make_jsonrpc_request('get_module_info_by_address', address)

@mcp.tool()
def get_module_info_by_name(name: Annotated[str, Field(description='Name of the module to get the info for')]) -> dict:
    """Get the module info for a given name"""
    return make_jsonrpc_request('get_module_info_by_name', name)

@mcp.tool()
def get_next_module_by_name(name: Annotated[str, Field(description='Name of the module to get the next module for')]) -> dict:
    """Get the next module in the database"""
    return make_jsonrpc_request('get_next_module_by_name', name)

@mcp.tool()
def add_bpt(address: Annotated[str, Field(description='Address to add the breakpoint at')]) -> None:
    """Add a breakpoint at the given address"""
    return make_jsonrpc_request('add_bpt', address)

@mcp.tool()
def del_bpt(address: Annotated[str, Field(description='Address to delete the breakpoint at')]) -> None:
    """Delete the breakpoint at the given address"""
    return make_jsonrpc_request('del_bpt', address)

@mcp.tool()
def enable_bpt(address: Annotated[str, Field(description='Address to enable the breakpoint at')]) -> None:
    """Enable the breakpoint at the given address"""
    return make_jsonrpc_request('enable_bpt', address)

@mcp.tool()
def disable_bpt(address: Annotated[str, Field(description='Address to disable the breakpoint at')]) -> None:
    """Disable the breakpoint at the given address"""
    return make_jsonrpc_request('disable_bpt', address)

@mcp.tool()
def exist_bpt(address: Annotated[str, Field(description='Address to check if the breakpoint exists at')]) -> bool:
    """Check if a breakpoint exists at the given address"""
    return make_jsonrpc_request('exist_bpt', address)

@mcp.tool()
def step_into() -> None:
    """Step into"""
    return make_jsonrpc_request('step_into')

@mcp.tool()
def continue_process() -> None:
    """Continue the process"""
    return make_jsonrpc_request('continue_process')

@mcp.tool()
def suspend_process() -> None:
    """Suspend the process"""
    return make_jsonrpc_request('suspend_process')

@mcp.tool()
def exit_process() -> None:
    """Exit the process"""
    return make_jsonrpc_request('exit_process')

@mcp.tool()
def step_over() -> None:
    """Step over"""
    return make_jsonrpc_request('step_over')

@mcp.tool()
def get_process_state() -> int:
    """Get the process state"""
    return make_jsonrpc_request('get_process_state')

@mcp.tool()
def read_dbg_memory(address: Annotated[str, Field(description='Address to read from')], size: Annotated[int, Field(description='Size to read in bytes')]) -> str:
    """Read memory from the debugger"""
    return make_jsonrpc_request('read_dbg_memory', address, size)

@mcp.tool()
def export_functions_to_file(filename: Annotated[str, Field(description='Path to the file to export to')], offset: Annotated[int, Field(description='Offset to start listing from (start at 0)')], count: Annotated[int, Field(description='Number of functions to list (100 is a good default, 0 means remainder)')]):
    """Export functions to a file"""
    return make_jsonrpc_request('export_functions_to_file', filename, offset, count)

@mcp.tool()
def get_prefix_functions(prefix: Annotated[str, Field(description='Prefix to filter functions by')], offset: Annotated[int, Field(description='Offset to start listing from (start at 0)')], count: Annotated[int, Field(description='Number of functions to list (100 is a good default, 0 means remainder)')]) -> Page[Function]:
    """Get functions with a specific prefix (paginated)"""
    return make_jsonrpc_request('get_prefix_functions', prefix, offset, count)

@mcp.tool()
def get_prefix_functions_count(prefix: Annotated[str, Field(description='Prefix to filter functions by')]) -> int:
    """Get the number of functions with a specific prefix"""
    return make_jsonrpc_request('get_prefix_functions_count', prefix)

@mcp.tool()
def get_function_count() -> int:
    """Get the number of functions in the database"""
    return make_jsonrpc_request('get_function_count')

@mcp.tool()
def export_prefix_functions_to_file(filename: Annotated[str, Field(description='Path to the file to export to')], prefix: Annotated[str, Field(description='Prefix to filter functions by')], offset: Annotated[int, Field(description='Offset to start listing from (start at 0)')], count: Annotated[int, Field(description='Number of functions to list (100 is a good default, 0 means remainder)')]):
    """export functions with a specific prefix to a file"""
    return make_jsonrpc_request('export_prefix_functions_to_file', filename, prefix, offset, count)

@mcp.tool()
def list_globals(filter: Annotated[str, Field(description='Filter to apply to the list. Case-insensitive contains or /regex/ syntax')], offset: Annotated[int, Field(description='Offset to start listing from (start at 0)')], count: Annotated[int, Field(description='Number of globals to list (100 is a good default, 0 means remainder)')]) -> Page[Global]:
    """List all globals in the database (paginated)"""
    return make_jsonrpc_request('list_globals', filter, offset, count)

@mcp.tool()
def list_strings(filter: Annotated[str, Field(description='Filter to apply to the list. Case-insensitive contains or /regex/ syntax')], offset: Annotated[int, Field(description='Offset to start listing from (start at 0)')], count: Annotated[int, Field(description='Number of strings to list (100 is a good default, 0 means remainder)')]) -> Page[String]:
    """List all strings in the database (paginated)"""
    return make_jsonrpc_request('list_strings', filter, offset, count)

@mcp.tool()
def decompile_function(address: Annotated[str, Field(description='Address of the function to decompile')]) -> str:
    """Decompile a function at the given address"""
    return make_jsonrpc_request('decompile_function', address)

@mcp.tool()
def disassemble_function(start_address: Annotated[str, Field(description='Address of the function to disassemble')]) -> str:
    """Get assembly code (address: instruction; comment) for a function"""
    return make_jsonrpc_request('disassemble_function', start_address)

@mcp.tool()
def get_xrefs_to(address: Annotated[str, Field(description='Address to get cross references to')]) -> list[Xref]:
    """Get all cross references to the given address"""
    return make_jsonrpc_request('get_xrefs_to', address)

@mcp.tool()
def get_entry_points() -> list[Function]:
    """Get all entry points in the database"""
    return make_jsonrpc_request('get_entry_points')

@mcp.tool()
def mark_fuction_green(address: Annotated[str, Field(description='Address of the function to mark')]):
    """Mark a function with green color"""
    return make_jsonrpc_request('mark_fuction_green', address)

@mcp.tool()
def mark_function_red(address: Annotated[str, Field(description='Address of the function to mark')]):
    """Mark a function with red color"""
    return make_jsonrpc_request('mark_function_red', address)

@mcp.tool()
def set_comment(address: Annotated[str, Field(description='Address in the function to set the comment for')], comment: Annotated[str, Field(description='Comment text')]):
    """Set a comment for a given address in the function disassembly and pseudocode"""
    return make_jsonrpc_request('set_comment', address, comment)

@mcp.tool()
def rename_local_variable(function_address: Annotated[str, Field(description='Address of the function containing the variable')], old_name: Annotated[str, Field(description='Current name of the variable')], new_name: Annotated[str, Field(description='New name for the variable (empty for a default name)')]):
    """Rename a local variable in a function"""
    return make_jsonrpc_request('rename_local_variable', function_address, old_name, new_name)

@mcp.tool()
def rename_global_variable(old_name: Annotated[str, Field(description='Current name of the global variable')], new_name: Annotated[str, Field(description='New name for the global variable (empty for a default name)')]):
    """Rename a global variable"""
    return make_jsonrpc_request('rename_global_variable', old_name, new_name)

@mcp.tool()
def set_global_variable_type(variable_name: Annotated[str, Field(description='Name of the global variable')], new_type: Annotated[str, Field(description='New type for the variable')]):
    """Set a global variable's type"""
    return make_jsonrpc_request('set_global_variable_type', variable_name, new_type)

@mcp.tool()
def rename_function(function_address: Annotated[str, Field(description='Address of the function to rename')], new_name: Annotated[str, Field(description='New name for the function (empty for a default name)')]):
    """Rename a function"""
    return make_jsonrpc_request('rename_function', function_address, new_name)

@mcp.tool()
def set_function_prototype(function_address: Annotated[str, Field(description='Address of the function')], prototype: Annotated[str, Field(description='New function prototype')]) -> str:
    """Set a function's prototype"""
    return make_jsonrpc_request('set_function_prototype', function_address, prototype)

@mcp.tool()
def declare_c_type(c_declaration: Annotated[str, Field(description='C declaration of the type. Examples include: typedef int foo_t; struct bar { int a; bool b; };')]):
    """Create or update a local type from a C declaration"""
    return make_jsonrpc_request('declare_c_type', c_declaration)

@mcp.tool()
def set_local_variable_type(function_address: Annotated[str, Field(description='Address of the function containing the variable')], variable_name: Annotated[str, Field(description='Name of the variable')], new_type: Annotated[str, Field(description='New type for the variable')]):
    """Set a local variable's type"""
    return make_jsonrpc_request('set_local_variable_type', function_address, variable_name, new_type)

@mcp.tool()
def dbg_get_registers() -> list[dict[str, str]]:
    """Get all registers and their values. This function is only available when debugging."""
    return make_jsonrpc_request('dbg_get_registers')

@mcp.tool()
def dbg_get_call_stack() -> list[dict[str, str]]:
    """Get the current call stack."""
    return make_jsonrpc_request('dbg_get_call_stack')

@mcp.tool()
def dbg_list_breakpoints():
    """
    List all breakpoints in the program.
    """
    return make_jsonrpc_request('dbg_list_breakpoints')

@mcp.tool()
def dbg_start_process() -> str:
    """Start the debugger"""
    return make_jsonrpc_request('dbg_start_process')

@mcp.tool()
def dbg_exit_process() -> str:
    """Exit the debugger"""
    return make_jsonrpc_request('dbg_exit_process')

@mcp.tool()
def dbg_continue_process() -> str:
    """Continue the debugger"""
    return make_jsonrpc_request('dbg_continue_process')

@mcp.tool()
def dbg_run_to(address: Annotated[str, Field(description='Run the debugger to the specified address')]) -> str:
    """Run the debugger to the specified address"""
    return make_jsonrpc_request('dbg_run_to', address)

@mcp.tool()
def dbg_set_breakpoint(address: Annotated[str, Field(description='Set a breakpoint at the specified address')]) -> str:
    """Set a breakpoint at the specified address"""
    return make_jsonrpc_request('dbg_set_breakpoint', address)

@mcp.tool()
def dbg_delete_breakpoint(address: Annotated[str, Field(description='del a breakpoint at the specified address')]) -> str:
    """del a breakpoint at the specified address"""
    return make_jsonrpc_request('dbg_delete_breakpoint', address)

@mcp.tool()
def dbg_enable_breakpoint(address: Annotated[str, Field(description='Enable or disable a breakpoint at the specified address')], enable: Annotated[bool, Field(description='Enable or disable a breakpoint')]) -> str:
    """Enable or disable a breakpoint at the specified address"""
    return make_jsonrpc_request('dbg_enable_breakpoint', address, enable)


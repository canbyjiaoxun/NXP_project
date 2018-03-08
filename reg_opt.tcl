#report_power -outfile signoff_power.rpt
set ffList ""
foreach_in_collection ff [all_registers] {
set name [get_property $ff full_name]
if {[regexp cm3_dpu_regfile $name] || [regexp ip_core1 $name]} {
lappend ffList $name
}
}

report_analysis_views
set_interactive_constraint_modes {FUNC_MODE}
foreach ffName $ffList {
  set_max_delay 8.5 -to $ffName
}

optDesign -postRoute
saveNetlist ../../../NETLIST/HVT/slow_NXP/10p/10.0/none_dft_hier/chip_ic1_netlist_signoff_opt.v
extractRC
rcOut -rc_corner RC_MAX -spef ../../../NETLIST/HVT/slow_NXP/10p/10.0/none_dft_hier/chip_ic1_slow_NXP_signoff_RC_MAX_opt.spef
#write_sdf ../../../NETLIST/HVT/slow_NXP/10p/10.0/none_dft_hier/chip_ic1_slow_NXP_signoff_opt.sdf
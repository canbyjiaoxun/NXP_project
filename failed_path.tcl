
#This is to set the FF at each stage
#including dpu_fetch, dpu_decode, dpu_alu, dpu_lsu, dpu_status. 
set ffList ""
foreach_in_collection ff [all_registers] {
set name [get_property $ff full_name]
if {[regexp cm3_dpu_fetch $name]} {
lappend ffList $name
}
}


#This is to count the failed path among each stage
#only count 5000 per end point because it would be too large if count all of them
#write the slack of each faild path into the list
set path [get_timing_paths -to $ffList -nworst 5000 -max_paths 1000 -slack_lesser_than 0]
#set path [get_timing_paths -to $ffList -nworst 1 -max_paths 1000 -slack_lesser_than 0]
#report_timing -to $ffList -nworst 1 -max_slack -0.050
#sizeof_collection $path
set slackList ""
foreach_in_collection p $path {
lappend slackList [get_property $p slack]
}
set outFile [open slack_5000_fetch_nega.rpt w]
#set outFile [open slack_5000_dec_nega.rpt w]
#set outFile [open slack_5000_exec_nega.rpt w]
#set outFile [open slack_5000_alu_nega.rpt w]
#set outFile [open slack_5000_lsu_nega.rpt w]
#set outFile [open slack_5000_status_nega.rpt w]
#set outFile [open slack_5000_regfile_nega.rpt w]
#set outFile [open slack_5000_regbank_nega.rpt w]
#set outFile [open slack_5000_etmintf_nega.rpt w]
puts $outFile $slackList
close $outFile
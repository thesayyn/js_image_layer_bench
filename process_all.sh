
before=$(./process.sh before_cold.log | jq '. | map(.total | sub("s$"; "") | tonumber) | [0] + .' ) 

after=$(./process.sh after_cold.log | jq '. | map(.total | sub("s$"; "") | tonumber)')


echo "before" $before
echo "after" $after

jq -n --argjson before "$before" --argjson after "$after" '
{
    "Before (rules_js 2.2.0)": $before,
    "After  (rules_js 2.3.5)": $after
}
' | python3 plot.py "cold.png"

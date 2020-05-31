# XYZCONV

A XYZ Ångström<->UA converter

## Examples

### Example 1 : convert  au.xyz from AU to Ångström

```bash
xyzconv < ua.xyz > ang.xyz --from ua --to ang
#Same as
xyzconv < ua.xyz > ang.xyz --from bohr --to ang
#Same as
xyzconv < ua.xyz > ang.xyz --from bohr
```

### Example 2 : convert  ang.xyz from Ångström to AU


```
xyzconv < ang.xyz > ua.xyz --from ang --to ua
#Same as
xyzconv < ang.xyz > ua.xyz --from ang --to bohr
#Same as
xyzconv < ang.xyz > ua.xyz --to bohr
```
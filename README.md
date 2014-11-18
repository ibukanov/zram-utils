zram-utils
==========

Service files and scripts to enable zram swap on Linux

Description
-----------

This is based on what Fedora's Anakonda installer is doing when one passes inst.zram=on to it. However this does not depend on kernel command line arguments, uses single device with multithreading enabled and allows to enable zram irrespective of the amount of available memory.

Installation
------------

Run `sudo ./setup install && sudo systemctl start zram && sudo systemctl enable zram`.

Alternatively build an rpm: `./setup rpm` and install using it:
`sudo yum install ~/rpmbuild/RPMS/zram-utils-... &&  sudo systemctl start zram && sudo systemctl enable zram` 

Check that 'zram-status' generates an output like:
```
status: enabled
compression: -66%
disksize: 2249M
compr_data_size: 0K
orig_data_size: 4K
mem_used_total: 12K
max_comp_streams: 2
comp_algorithm: [lzo] 
```

Here the compression is negative as zram compressed a single page but use quite a few more pages for own support structures.
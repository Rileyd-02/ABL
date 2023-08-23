#!/usr/bin/env python
# coding: utf-8

# In[ ]:


if current_diff in cumulative_diff:
    subarray_length = i - cumulative_diff[current_diff]
    max_length = max(max_length, subarray_length)
else:
    cumulative_diff[current_diff] = i
    return max_length


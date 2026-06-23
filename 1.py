def is_isomorphic(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    map_s_to_t = {}
    map_t_to_s = {}

    for ch_s, ch_t in zip(s, t):
        if ch_s in map_s_to_t:
            if map_s_to_t[ch_s] != ch_t:
                return False
        else:
            map_s_to_t[ch_s] = ch_t

        if ch_t in map_t_to_s:
            if map_t_to_s[ch_t] != ch_s:
                return False
        else:
            map_t_to_s[ch_t] = ch_s

    return True

print(is_isomorphic("paper", "title"))

# сложноть O(n)
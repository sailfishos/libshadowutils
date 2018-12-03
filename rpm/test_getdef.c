#include "getdef.h"

#include <stdio.h>

int
get_or_fail(const char *key)
{
    int result = getdef_num(key, -1);
    if (result == -1) {
        fprintf(stderr, "ERROR: Cannot get value for '%s'\n", key);
        exit(1);
    }
    return result;
}

int
main(int argc, char *argv[])
{
    int uid_min = get_or_fail("UID_MIN");
    int uid_max = get_or_fail("UID_MAX");

    fprintf(stdout, "User ID Range: %d..%d\n", uid_min, uid_max);
    return 0;
}

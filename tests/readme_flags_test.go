package readme_flags_test

import (
    "os"
    "path/filepath"
    "regexp"
    "testing"
)

func TestReadmeUsesDocumentedGroupFlag(t *testing.T) {
    readmePath := filepath.Join("..", "README.md")
    data, err := os.ReadFile(readmePath)
    if err != nil {
        t.Fatalf("reading README.md: %v", err)
    }
    content := string(data)

    // --groups is documented; --group (singular) is not.
    if regexp.MustCompile(`(\W|^)--group(\W|$)`).MatchString(content) {
        t.Errorf("README.md contains undocumented --group flag; use --groups")
    }
    if !regexp.MustCompile(`(\W|^)--groups(\W|$)`).MatchString(content) {
        t.Errorf("README.md should mention --groups flag")
    }
